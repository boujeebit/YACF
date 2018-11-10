import graphene
from graphene_django import DjangoObjectType
# from gqlauth.validators import validate_username, validate_password, validate_user_is_authenticated
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from categories.models import Category
from challenges.models import Challenge

class ChallengeType(DjangoObjectType):
    class Meta:
        model = Challenge

class Query(graphene.ObjectType):
    all_challenges = graphene.List(ChallengeType)

    challenge = graphene.Field(ChallengeType, id=graphene.Int())
    statistic = graphene.Field(ChallengeType, category=graphene.String(), points=graphene.Int())

    def resolve_all_challenges(self, info, **kwargs):
        return Challenge.objects.all()

    def resolve_challenge(self, info, **kwargs):
        return Challenge.objects.get(pk=kwargs.get('id'))

    def resolve_statistic(self, info, **kwargs):
        # get_category = Category.objects.get( name__iexact=kwargs.get('category')
        # print(Category.objects.get( name__iexact=kwargs.get('category'))
        get_category = Category.objects.get( name__iexact=kwargs.get('category'))
        return Challenge.objects.filter(category=get_category, points=kwargs.get('points')).first()
        # return Challenge.objects.filter( points=kwargs.get('points') ).first()
        # return Challenge.objects.get(pk=1)

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
    def mutate(self, info, name, description, points=0, flag="", show=False, category=None):
        try:
            if category:
                try:
                    category = Category.objects.get(name=category)
                    newChallenge = Challenge(name=name, description=description, points=points, flag=flag, show=show, category=category)
                    newChallenge.save()
                except:
                    # Category not found
                    message = "failure"
            else:
                newChallenge = Challenge(name=name, description=description, points=points, flag=flag, show=show)
                newChallenge.save()
            message = "success"
        except:
            message = "failure"

        return AddChallenge(message)

class SubmitFlag(graphene.Mutation):
    code = graphene.Int()

    class Arguments:
        #DOC: Challenge will equeal the PK of the challenge a.k.a id
        challenge   = graphene.Int(required=True)
        flag        = graphene.String(required=True)


    def mutate(self, info, challenge, flag):

        try:
            get_challenge = Challenge.objects.get(pk=challenge)
            if get_challenge.flag == flag:
                code = 1
            else:
                code = 0
        except:
            code = 9

        return SubmitFlag(code)


class Mutation(object):
    addChallenge = AddChallenge.Field()
    submitflag = SubmitFlag.Field()