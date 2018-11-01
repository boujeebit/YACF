import graphene

import uauth.schema

class Query(uauth.schema.Query, graphene.ObjectType):
    pass

class Mutation(uauth.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)