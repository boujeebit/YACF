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

    def resolve_all_teams(self, info, **kwargs):
        
        channel_layer = channels.layers.get_channel_layer()
        # Send message to WebSocket
        async_to_sync(channel_layer.group_send)("socreboard", {"type": "scoreboard.update", "team": "blue", "points": "1000", "added": "100"} )

        # await channel_layer.send(
        #     chat_message,
        #     {"type": "chat.system_message", "text": "boom"},
        # )



        return Team.objects.all()

    def resolve_team(self, info, **kwargs):
        return Team.objects.get(name__iexact=kwargs.get('name'))
    
    def resolve_all_solves(self, info, **kwargs):
        return SolvedChallenge.objects.all()
    

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

class Mutation(object):
    addteam = AddTeam.Field()