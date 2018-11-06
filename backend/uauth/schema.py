import graphene
from graphene_django import DjangoObjectType
# from gqlauth.validators import validate_username, validate_password, validate_user_is_authenticated
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def validate_user_is_authenticated(user):
    if user.is_anonymous:
        raise Exception('Not authenticated')

class Me(DjangoObjectType):
    class Meta:
        model = User

class Query(object):
    me = graphene.Field(Me)

    def resolve_me(self, info):
        user = info.context.user
        validate_user_is_authenticated(user)

        return user

# ------------------- MUTATIONS -------------------


class LogIn(graphene.Mutation):
    id = graphene.Int()
    isAuthenticated = graphene.Int()

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, username, password):
        # Validate username and password
        #validate_username(username)
        #validate_password(password)

        user = authenticate(username=username, password=password)

        if not user:
            raise Exception('Invalid username or password')

        login(info.context, user)

        return LogIn(id=user.id,)
    
class LogOut(graphene.Mutation):
    status = graphene.String()

    def mutate(self, info):
        logout(info.context) 
        return LogOut(status='Logged Out')

class Mutation(object):
    login = LogIn.Field()
    logout = LogOut.Field()