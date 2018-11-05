import graphene
from graphene_django import DjangoObjectType
from challenges.models import Challenge  
from uauth.validators import validate_user_is_authenticated
from challenges.validators import validate_name, validate_description, validate_points, validate_create_flag, validate_check_flag


class ChallengeType(DjangoObjectType):
    class Meta:
        model = Challenge

class Query(graphene.ObjectType):
    all_challenges = graphene.List(ChallengeType)

    def resolve_all_challenges(self, info, **kwargs):
        return Challenge.objects.all()

# ------------------- MUTATIONS -------------------

class AddChallenge(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        name        = graphene.String(required=True)
        description = graphene.String(required=True)
        flag        = graphene.String(required=True)
        points      = graphene.Int(required=True)
        show        = graphene.Boolean(required=False)

    def mutate(self, info, name, description, flag, points, show=False):
        # Convert flag to lower case
        flag = flag.lower()

        # Validate user input
        validate_name(name)
        validate_description(description)
        validate_create_flag(flag)
        validate_points(points)

        try:
            newChallenge = Challenge(name=name, description=description, points=points, flag=flag, show=show)
            newChallenge.save()
            message = "success"
        except:
            message = "failure"

        return AddChallenge(message)

class CheckFlag(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        flag        = graphene.String(required=True)


    def mutate(self, info, flag):
        user = info.user

        # Convert flag to lower case
        flag = flag.lower()

        # Verify user is authenticated
        validate_user_is_authenticated(user)

        # Validate user input
        validate_check_flag(flag)

        try:
            if Challenge.objects.filter(flag__iexact=flag.exists()):
                                
                message = "Correct Flag"
            else:
                message = "Wrong Flag"
        except: 
            message = "failure"

        return AddChallenge(message)

class Mutation(object):
    addChallenge = AddChallenge.Field()
    checkFlag = CheckFlag.Field()