import graphene

import links.schema
import users.schema

#get data
class Query(links.schema.Query, graphene.ObjectType):
    pass

#insert data
class Mutation(users.schema.Mutation, links.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)