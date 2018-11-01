import graphene

import uauth.schema
import categories.schema

class Query(uauth.schema.Query, categories.schema.Query, graphene.ObjectType):
    pass

class Mutation(uauth.schema.Mutation, categories.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)