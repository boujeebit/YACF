import graphene
from graphene_django import DjangoObjectType
from uauth.validators import validate_user_is_authenticated, validate_user_is_admin

from pages.models import Page

import json

class PageType(DjangoObjectType):
    class Meta:
        model = Page

class Query(graphene.ObjectType):
    pages = graphene.List(PageType)
    page = graphene.Field(PageType, url=graphene.String())

    def resolve_pages(self, info, **kwargs):
        validate_user_is_authenticated(info.context.user)
        return Page.objects.all()

    def resolve_page(self, info, **kwargs):
        validate_user_is_authenticated(info.context.user)
        return Page.objects.get(url=kwargs.get('url'))

# ------------------- MUTATIONS -------------------

class CreatePage(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        name = graphene.String(required=True)
        url = graphene.String(required=True)
        content = graphene.String(required=True)

    def mutate(self, info, name, url, content):
        validate_user_is_admin(info.context.user)
        
        page = Page(name=name, url=url, content=content)
        page.save()

        return CreatePage(message="Added")

class Mutation(object):
    createpage = CreatePage.Field()