import graphene
from graphene_django import DjangoObjectType
from uauth.validators import validate_user_is_authenticated, validate_user_is_admin

from server.models import Theme

class ThemeType(DjangoObjectType):
    class Meta:
        model = Theme

class Query(graphene.ObjectType):
    theme = graphene.Field(ThemeType)
    
    def resolve_theme(self, info, **kwargs):
        validate_user_is_authenticated(info.context.user)
        return Theme.objects.first()
