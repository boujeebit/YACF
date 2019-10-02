import graphene
from graphene_django import DjangoObjectType
from uauth.validators import validate_user_is_authenticated, validate_user_is_admin
import json

from index.models import WelcomePage

class WelcomePageType(DjangoObjectType):
    class Meta:
        model = WelcomePage

class Query(graphene.ObjectType):
    welcomePage = graphene.Field(WelcomePageType)

    def resolve_welcomePage(self, info, **kwargs):
        validate_user_is_authenticated(info.context.user)
        return WelcomePage.objects.all().first()

# ------------------- MUTATIONS -------------------

class Welcome(graphene.Mutation):
    status = graphene.String()

    class Arguments:
        content = graphene.String(required=True)

    def mutate(self, info, content):
        validate_user_is_admin(info.context.user)
        welcome = WelcomePage.objects.all().first()
        if welcome:
            welcome.content = content
            welcome.save()
        else:
            welcome = WelcomePage(content=content)
            welcome.save()

        return Welcome(status="Added")

class Mutation(object):
    welcome = Welcome.Field()