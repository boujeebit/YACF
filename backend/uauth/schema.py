import graphene
from graphene_django import DjangoObjectType
from uauth.validators import validate_user_is_authenticated, validate_user_is_admin
from django.contrib.auth import authenticate, login, logout
# from uauth.validators import authenticate
from django.contrib.auth.models import User
from uauth.models import Profile

from teams.models import Team

def validate_user_is_authenticated(user):
    if user.is_anonymous:
        raise Exception('Not authenticated')

class Me(DjangoObjectType):
    class Meta:
        model = User
        exclude_fields = ('password')

class Query(object):
    all_users = graphene.List(Me)
    me = graphene.Field(Me)

    def resolve_all_users(self, info):
        validate_user_is_admin(info.context.user)
        return User.objects.all()

    def resolve_me(self, info):
        validate_user_is_authenticated(info.context.user)
        return user

# ------------------- MUTATIONS -------------------


class AddUser(graphene.Mutation):
    code = graphene.Int()

    class Arguments:
        username   = graphene.String(required=True)
        email      = graphene.String(required=True)
        password   = graphene.String(required=True)
        firstname  = graphene.String(required=True)
        lastname   = graphene.String(required=True)
        accesscode = graphene.String(required=True)

    # TODO: VALIDATION CHECK!!
    # TODO: TRY CATCH
    def mutate(self, info, username, email, password, firstname, lastname, accesscode):
        validate_user_is_admin(info.context.user)
        team = Team.objects.filter(accesscode=accesscode).first()
        if team:
            newUser = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
            newProfile = Profile(user=newUser, verified=False, team=team, hidden=False)
            newProfile.save()
            code = 0
        else:
            # Invaild access code
            code = 1

        login(info.context, newUser)

        return AddUser(code=code)

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
    adduser = AddUser.Field()
    login   = LogIn.Field()
    logout  = LogOut.Field()