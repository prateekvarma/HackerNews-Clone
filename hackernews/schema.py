import graphene

import links.schema

#get data
class Query(links.schema.Query, graphene.ObjectType):
    pass

#insert data
class Mutation(links.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)