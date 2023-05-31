
from graphene_django import DjangoObjectType
from .models import Todo

class TodoType(DjangoObjectType):
    """GraphQL type representing the Todo model."""
    class Meta:
        model = Todo
