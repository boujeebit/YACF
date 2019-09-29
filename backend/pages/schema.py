import graphene
from graphene_django import DjangoObjectType
# from gqlauth.validators import validate_username, validate_password, validate_user_is_authenticated
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from pages.models import Page

import json

from pages.models import Page

class PageType(DjangoObjectType):
    class Meta:
        model = Page

class Query(graphene.ObjectType):
    pages = graphene.List(PageType)
    page = graphene.Field(PageType, url=graphene.String())

    def resolve_pages(self, info, **kwargs):
        return Page.objects.all()

    def resolve_page(self, info, **kwargs):
        return Page.objects.get(url=kwargs.get('url'))

# ------------------- MUTATIONS -------------------

class CreatePage(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        name = graphene.String(required=True)
        url = graphene.String(required=True)
        content = graphene.String(required=True)

    def mutate(self, info, name, url, content):
        page = Page(name=name, url=url, content=content)
        page.save()

        return CreatePage(message="Added")

class Mutation(object):
    createpage = CreatePage.Field()