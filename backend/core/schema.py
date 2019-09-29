import graphene

import uauth.schema
import categories.schema
import challenges.schema
import teams.schema
import index.schema
import server.schema
import pages.schema

class Query(uauth.schema.Query, categories.schema.Query, challenges.schema.Query, teams.schema.Query, index.schema.Query, server.schema.Query, pages.schema.Query, graphene.ObjectType):
    pass

class Mutation(uauth.schema.Mutation, categories.schema.Mutation, challenges.schema.Mutation, teams.schema.Mutation, index.schema.Mutation, pages.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)