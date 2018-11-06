import graphene

import uauth.schema
import categories.schema
import challenges.schema
import teams.schema

class Query(uauth.schema.Query, categories.schema.Query, challenges.schema.Query, teams.schema.Query, graphene.ObjectType):
    pass

class Mutation(uauth.schema.Mutation, categories.schema.Mutation, challenges.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)