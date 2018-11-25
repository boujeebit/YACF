import channels.layers
from asgiref.sync import async_to_sync

import graphene
from graphene_django import DjangoObjectType
# from gqlauth.validators import validate_username, validate_password, validate_user_is_authenticated
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from uauth.models import Profile

import json

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

    team_sovle = graphene.List(SolvedChallengeType)

    # graph = graphene.List(TeamType)

    def resolve_all_teams(self, info, **kwargs):
        return Team.objects.all()

    def resolve_team(self, info, **kwargs):
        return Team.objects.get(name__iexact=kwargs.get('name'))
    
    def resolve_all_solves(self, info, **kwargs):
        return SolvedChallenge.objects.all()

    def resolve_team_sovle(self, info, **kwargs):
        profile = Profile.objects.get(user=info.context.user)
        return SolvedChallenge.objects.filter(team=profile.team)


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
    timeline = graphene.String()
    message = graphene.String()

    class Arguments:
        number = graphene.Int(required=False)

    def mutate(self, info, number=10):

        # Sort to get the top 5 by point value
        teams = sorted(list(Team.objects.all()), key=lambda x: x.points, reverse=True)[:5]

        # Get all solved challenges from the top 5 teams.
        solved = SolvedChallenge.objects.filter(team__name__in=[team.name for team in teams]).order_by('timestamp')

        graph = []
        for team in teams:
            graph.append({'label': team.name, 'data': [], 'backgroundColor': '', 'borderColor': '', 'fill': 'false'})

        colors = ['#FFD700', '#909497', '#A46628', '#3232CD', '#93C54B']

        # Build colors
        for i, team in enumerate(graph):
            team['backgroundColor'] = colors[i]
            team['borderColor'] = colors[i]


        # Construct the data for solved timelinw
        for solve in solved:

            for team in graph:
                if team["label"] == solve.team.name:
                    if team['data']:
                        team['data'].append(team['data'][-1]+solve.challenge.points)
                    else:
                        team['data'].append(solve.challenge.points)
                else:
                    if team['data']:
                        team['data'].append(team['data'][-1])
                    else:
                        team['data'].append(0)


        # Construct time for all solved challenges.
        timeline = []
        for solve in solved:
            timeline.append(solve.timestamp.strftime("%I:%M:%S"))


        return Graph(json.dumps(timeline), json.dumps(graph))

class Mutation(object):
    addteam = AddTeam.Field()
    graph   = Graph.Field()