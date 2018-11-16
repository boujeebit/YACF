import channels.layers
from asgiref.sync import async_to_sync

import graphene
from graphene_django import DjangoObjectType
# from gqlauth.validators import validate_username, validate_password, validate_user_is_authenticated
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Team, SolvedChallenge

class TeamType(DjangoObjectType):
    points = graphene.Int()
    correct_flags = graphene.Int()

    class Meta:
        model = Team

class SolvedChallengeType(DjangoObjectType):
    class Meta:
        model = SolvedChallenge

class Query(graphene.ObjectType):
    all_teams = graphene.List(TeamType)
    all_solves = graphene.List(SolvedChallengeType)

    team = graphene.Field(TeamType, name=graphene.String())

    # graph = graphene.List(TeamType)

    def resolve_all_teams(self, info, **kwargs):
        return Team.objects.all()

    def resolve_team(self, info, **kwargs):
        return Team.objects.get(name__iexact=kwargs.get('name'))
    
    def resolve_all_solves(self, info, **kwargs):
        return SolvedChallenge.objects.all()

    # def resolve_graph(self, info, **kwargs):
    #     return Team.objects.filter(points=8700)   

# ------------------- MUTATIONS -------------------


class AddTeam(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        name        = graphene.String(required=True)
        accesscode  = graphene.String(required=False)

    def mutate(self, info, name, accesscode=None):
        try:
            if not accesscode:
                accesscode = "This Needs to be generated (teams/schema.py)"

            newTeam = Team(name=name, accesscode=accesscode)
            newTeam.save()
            message = "success"
        except:
            message = "failure"

        return AddTeam(message)

class Graph(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        number = graphene.Int(required=False)

    def mutate(self, info, number=10):

        # Sort to get the top 5 by point value
        teams = sorted(list(Team.objects.all()), key=lambda x: x.points, reverse=True)[:5]

        # Get all solved challenges from the top 5 teams.
        challenges = SolvedChallenge.objects.filter(team__name__in=[team.name for team in teams]).order_by('-timestamp')

        # timechal = sorted(list(challenges), key=lambda x: x.timestamp, reverse=True)

        print(challenges)

        for challenge in challenges:
            # print(dir(challenge.team.all))
            print(challenge.team.all())

        return Graph("message")

class Mutation(object):
    addteam = AddTeam.Field()
    graph   = Graph.Field()