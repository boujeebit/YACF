import channels.layers
from asgiref.sync import async_to_sync

import hashlib
import graphene
from graphene_django import DjangoObjectType
from uauth.validators import validate_user_is_authenticated, validate_user_is_admin, validate_user_is_staff

from categories.models import Category
from challenges.models import Challenge, Flag, Hint
from teams.models import SolvedChallenge, Failure
from uauth.models import Profile

class ChallengeType(DjangoObjectType):
    class Meta:
        model = Challenge
        exclude_fields = ('flag')

class FlagType(DjangoObjectType):
    class Meta:
        model = Flag

class HintType(DjangoObjectType):
    class Meta:
        model = Hint

    '''
    TODO: Need a catch all for non staff, show nothing
    '''
    def resolve_content(self, info):
        if not self.hidden:
            return self.content
        else:
            return ''

class Query(graphene.ObjectType):
    challenges = graphene.List(ChallengeType)
    challenge = graphene.Field(ChallengeType, id=graphene.Int())

    statistic = graphene.Field(ChallengeType, category=graphene.String(), points=graphene.Int())
    total_points = graphene.Int()

    def resolve_challenges(self, info, **kwargs):
        validate_user_is_authenticated(info.context.user)
        if validate_user_is_staff(info.context.user):
            return Challenge.objects.all().order_by('points')
        else:
            return Challenge.objects.filter(category__hidden=False, hidden=False).order_by('points')

    def resolve_challenge(self, info, **kwargs):
        validate_user_is_authenticated(info.context.user)
        return Challenge.objects.get(pk=kwargs.get('id'))


    def resolve_statistic(self, info, **kwargs):
        validate_user_is_authenticated(info.context.user)
        get_category = Category.objects.get( name__iexact=kwargs.get('category') )
        return Challenge.objects.filter(category=get_category, points=kwargs.get('points')).first()

    def resolve_total_points(self, info, **kwargs):
        validate_user_is_authenticated(info.context.user)
        return sum([challenge.points for challenge in Challenge.objects.all()])


# ------------------- MUTATIONS -------------------

class AddChallenge(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        name        = graphene.String(required=True)
        description = graphene.String(required=True)
        points      = graphene.Int(required=False)
        flag        = graphene.String(required=False)
        show        = graphene.Boolean(required=False)

        category    = graphene.String(required=False)

    #TODO: Need to check and ensure no challenge is made with the same points as another challenge. If not, frontend stats break
    #TODO: Just fix the frontend :) ^^
    def mutate(self, info, name, description, points=0, flag="", show=False, category=None):
        validate_user_is_admin(info.context.user)

        try:
            if category:
                try:
                    category = Category.objects.get(name=category)
                    newChallenge = Challenge(name=name, description=description, points=points, show=show, category=category)
                    newChallenge.save()
                    flag = Flag(value=hashlib.md5(flag.encode('utf-8')).hexdigest(), challenge=newChallenge)
                    flag.save()
                except:
                    # Category not found
                    message = "failure"
            else:
                newChallenge = Challenge(name=name, description=description, points=points, show=show)
                newChallenge.save()
                flag = Flag(value=flag, challenge=newChallenge)
                flag.save()

            message = "success"
        except:
            message = "failure"

        return AddChallenge(message)

class RemoveChallenge(graphene.Mutation):
    code = graphene.Int()

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        validate_user_is_admin(info.context.user)

        try:
            challenge = Challenge.objects.get(pk=id)
            challenge.delete()
            code = 0
        except:
            code = 1

        return RemoveChallenge(code)

class UpdateChallenge(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        id          = graphene.Int(required=True)
        name        = graphene.String(required=True)
        description = graphene.String(required=True)
        points      = graphene.Int(required=False)
        flag        = graphene.String(required=False)
        show        = graphene.Boolean(required=False)

        category    = graphene.String(required=False)

    #TODO: Need to check and ensure no challenge is made with the same points as another challenge. If not, frontend stats break
    def mutate(self, info, id, name, description, points=0, flag="", show=False, category=None):
        validate_user_is_admin(info.context.user)

        try:
            category = Category.objects.get(name=category)
            challenge = Challenge.objects.get(pk=id)
            challenge.name = name
            challenge.description = description
            challenge.points = points
            challenge.flag = flag
            challenge.show = show
            challenge.category = category

            challenge.save()


            message = "success"
        except:
            message = "failure"

        return UpdateChallenge(message)


class SubmitFlag(graphene.Mutation):
    code = graphene.Int()

    class Arguments:
        #DOC: Challenge will equal the PK of the challenge a.k.a id
        challenge   = graphene.Int(required=True)
        flag        = graphene.String(required=True)


    def mutate(self, info, challenge, flag):
        validate_user_is_authenticated(info.context.user)

        print("User:", info.context.user)
        # print("Team:", info.context.user.profile.verified)
        team = Profile.objects.get(user=info.context.user).team
        print("Team:", team.name)
        try:
            get_challenge = Challenge.objects.get(pk=challenge)
            if get_challenge.flag.value == hashlib.md5(flag.encode('utf-8')).hexdigest():
                if team:
                    solve = SolvedChallenge(team=team, user=info.context.user, challenge=get_challenge)
                    solve.save()                  
                code = 1
            else:
                if team:
                    fail = Failure(team=team, user=info.context.user, challenge=get_challenge)
                    fail.save()
                code = 0
        except:
            code = 9


        if code == 1:
            try:
                # Send signal to scoreboard
                channel_layer = channels.layers.get_channel_layer()
                async_to_sync(channel_layer.group_send)("scoreboard", {"type": "scoreboard.update", "team": team.name, "points": team.points, "added": get_challenge.points, "time": solve.timestamp.strftime("%I:%M:%S")} )
            except:
                pass

        return SubmitFlag(code)


class Mutation(object):
    addChallenge = AddChallenge.Field()
    removeChallenge = RemoveChallenge.Field()
    updateChallenge = UpdateChallenge.Field()
    submitflag = SubmitFlag.Field()