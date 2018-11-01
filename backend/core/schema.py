import graphene

class Query():
    pass

class Mutation():
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)