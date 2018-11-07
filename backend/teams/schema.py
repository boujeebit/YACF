import graphene
from graphene_django import DjangoObjectType
# from gqlauth.validators import validate_username, validate_password, validate_user_is_authenticated
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Team, SolvedChallenge

class TeamType(DjangoObjectType):
    class Meta:
        model = Team

class SolvedChallengeType(DjangoObjectType):
    class Meta:
        model = SolvedChallenge

class Query(graphene.ObjectType):
    all_teams = graphene.List(TeamType)
    all_solved_challenges = graphene.List(TeamType)

    team = graphene.Field(TeamType, name=graphene.String())

    def resolve_all_teams(self, info, **kwargs):
        return Team.objects.all()

    def resolve_team(self, info, **kwargs):
        return Team.objects.filter(name=kwargs.get('name')).first()
    
    def all_solved_challenges(self, info, **kwargs):
        return SolvedChallenge.objects.all()
    

# ------------------- MUTATIONS -------------------


# class AddCategory(graphene.Mutation):
#     message = graphene.String()

#     class Arguments:
#         name        = graphene.String(required=True)
#         description = graphene.String(required=True)

#     def mutate(self, info, name, description):
#         try:
#             newCategory = Category(name=name, description=description)
#             newCategory.save()
#             message = "success"
#         except:
#             message = "failure"

#         return AddCategory(message)

# class Mutation(object):
#     getteam = GetTeam.Field()