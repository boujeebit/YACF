import graphene
from graphene_django import DjangoObjectType
# from gqlauth.validators import validate_username, validate_password, validate_user_is_authenticated
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

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