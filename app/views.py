from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

@csrf_exempt
def graphql_view(request):
    return GraphQLView.as_view(graphiql=True)(request)
