import channels.layers
from asgiref.sync import async_to_sync

import graphene
from graphene_django import DjangoObjectType
# from gqlauth.validators import validate_username, validate_password, validate_user_is_authenticated
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from uauth.models import Profile

import string, random

import json

from .models import Team, SolvedChallenge

class TeamType(DjangoObjectType):
    points = graphene.Int()
    members = graphene.Int()
    correct_flags = graphene.Int()

    class Meta:
        model = Team

class SolvedChallengeType(DjangoObjectType):
    class Meta:
        model = SolvedChallenge

class Query(graphene.ObjectType):
    all_teams = graphene.List(TeamType)
    all_solves = graphene.List(SolvedChallengeType)

    team_name = graphene.Field(TeamType, name=graphene.String())
    team = graphene.Field(TeamType)

    team_sovle = graphene.List(SolvedChallengeType)

    # graph = graphene.List(TeamType)

    def resolve_all_teams(self, info, **kwargs):
        return Team.objects.all()

    def resolve_team_name(self, info, **kwargs):
        return Team.objects.get(name__iexact=kwargs.get('name'))

    def resolve_team(self, info, **kwargs):
        return info.context.user.profile.team
    
    def resolve_all_solves(self, info, **kwargs):
        return SolvedChallenge.objects.all()

    def resolve_team_sovle(self, info, **kwargs):
        profile = Profile.objects.get(user=info.context.user)
        return SolvedChallenge.objects.filter(team=profile.team)


# ------------------- MUTATIONS -------------------


class AddTeam(graphene.Mutation):
    code = graphene.Int()

    class Arguments:
        name        = graphene.String(required=True)
        email       = graphene.String(required=True)
        affiliation = graphene.String(required=True)
        # accesscode  = graphene.String(required=False)

    # TODO: VALIDATION CHECK!!
    def mutate(self, info, name, email, affiliation): #, accesscode=None):
        try:
            newTeam = Team(name=name, email=email, affiliation=affiliation, accesscode=''.join(random.choices(string.ascii_uppercase + string.digits, k=10)))
            newTeam.save()
            code = 0
        except:
            code = 1

        return AddTeam(code)

class UpdateTeam(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        id          = graphene.Int(required=True)
        name        = graphene.String(required=True)
        affiliation = graphene.String(required=True)
        email       = graphene.String(required=True)
        website     = graphene.String(required=True)
        accesscode  = graphene.String(required=True)
        

    # TODO: VALIDATION CHECK!!
    # TODO: Make it so it is not need to submit every state to change the info
    def mutate(self, info, id, name, affiliation, email, website, accesscode): #, accesscode=None):
        try:
            team = Team.objects.get(pk=id)
            team.name = name
            team.affiliation = affiliation
            team.email = email
            team.website = website
            team.accesscode = accesscode
            team.save()

            message = "success"
        except:
            message = "failure"

        return UpdateTeam(message)

class RemoveTeam(graphene.Mutation):
    code = graphene.Int()

    class Arguments:
        name        = graphene.String(required=True)

    # TODO: VALIDATION CHECK!!
    def mutate(self, info, name): #, accesscode=None):
        try:
            team = Team.objects.get(name=name)
            team.delete()
            code = 0
        except:
            code = 1

        return RemoveTeam(code)


#TODO: Move to queries
class TeamGraph(graphene.Mutation):
    timeline = graphene.String()
    message = graphene.String() 

    class Arguments:
        name = graphene.String(required=True)

    def mutate(self, info, name):
        team = Team.objects.get(name__iexact=name)
        # print(team)
        # print(team.solved.all().order_by('timestamp'))


        graph = [{'label': team.name, 'data': [], 'backgroundColor': '#FFD700', 'borderColor': '#FFD700', 'fill': 'false'}]

        for solve in team.solved.all().order_by('timestamp'):
            if graph[0]['data']:
                graph[0]['data'].append(graph[0]['data'][-1]+solve.challenge.points)
            else:
                graph[0]['data'].append(solve.challenge.points)

        timeline = []
        for solve in team.solved.all().order_by('timestamp'):
            timeline.append(solve.timestamp.strftime("%I:%M:%S"))

        # print(graph, timeline)

        return TeamGraph(json.dumps(timeline), json.dumps(graph))




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
    removeteam = RemoveTeam.Field()
    updateteam = UpdateTeam.Field()
    teamgraph = TeamGraph.Field()
    graph   = Graph.Field()