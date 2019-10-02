import graphene
from graphene_django import DjangoObjectType
from uauth.validators import validate_user_is_authenticated, validate_user_is_admin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Category

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class Query(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)

    def resolve_all_categories(self, info, **kwargs):
        validate_user_is_authenticated(info.context.user)
        return Category.objects.all()

# ------------------- MUTATIONS -------------------

class AddCategory(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        name        = graphene.String(required=True)
        description = graphene.String(required=True)

    def mutate(self, info, name, description):
        validate_user_is_admin(info.context.user)
        try:
            newCategory = Category(name=name, description=description)
            newCategory.save()
            message = "success"
        except:
            message = "failure"

        return AddCategory(message)

class RemoveCategory(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        validate_user_is_admin(info.context.user)
        try:
            category = Category.objects.get(pk=id)
            category.delete()
            message = "success"
        except:
            message = "failure"

        return RemoveCategory(message)

class UpdateCategory(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        id          = graphene.Int(required=True)
        name        = graphene.String(required=True)
        description = graphene.String(required=True)

    def mutate(self, info, id, name, description):
        validate_user_is_admin(info.context.user)
        try:
            category = Category.objects.get(pk=id)
            category.name = name
            category.description = description
            category.save()
            message = "success"
        except:
            message = "failure"

        return UpdateCategory(message)

class Mutation(object):
    addcategory = AddCategory.Field()
    removeCategory = RemoveCategory.Field()
    updateCategory = UpdateCategory.Field()