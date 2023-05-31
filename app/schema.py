import graphene
from .models import Todo
from .types import TodoType
from .mutations import CreateTodoMutation, DeleteTodoMutation, UpdateTodoMutation

class Query(graphene.ObjectType):
    """GraphQL query class."""
    todos = graphene.List(TodoType)

    def resolve_todos(self, info):
        """Retrieve all Todos."""
        return Todo.objects.all()

class Mutation(graphene.ObjectType):
    """GraphQL mutation class."""
    create_todo = CreateTodoMutation.Field()
    update_todo = UpdateTodoMutation.Field()
    delete_todo = DeleteTodoMutation.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)
