import graphene
from graphene_django import DjangoObjectType
# from gqlauth.validators import validate_username, validate_password, validate_user_is_authenticated
from django.contrib.auth import authenticate, login, logout

from server.models import Theme

class ThemeType(DjangoObjectType):
    class Meta:
        model = Theme

class Query(graphene.ObjectType):
    theme = graphene.Field(ThemeType)
    
    def resolve_theme(self, info, **kwargs):
        return Theme.objects.first()
