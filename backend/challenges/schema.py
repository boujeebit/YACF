import graphene
from graphene_django import DjangoObjectType
# from gqlauth.validators import validate_username, validate_password, validate_user_is_authenticated
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Challenge

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
        points      = graphene.Int(required=False)
        flag        = graphene.String(required=False)
        show        = graphene.Boolean(required=False)

    def mutate(self, info, name, description, points=0, flag="", show=False):
        try:
            newChallenge = Challenge(name=name, description=description, points=points, flag=flag, show=show)
            newChallenge.save()
            message = "success"
        except:
            message = "failure"

        return AddChallenge(message)

class Mutation(object):
    addChallenge = AddChallenge.Field()