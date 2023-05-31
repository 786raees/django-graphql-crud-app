import graphene
from .models import Todo
from .types import TodoType

class CreateTodoMutation(graphene.Mutation):
    """Mutation for creating a new Todo."""
    class Arguments:
        title = graphene.String()
        description = graphene.String()

    todo = graphene.Field(TodoType)

    def mutate(self, info, title, description):
        """Create a new Todo with the given title and description."""
        todo = Todo.objects.create(title=title, description=description)
        return CreateTodoMutation(todo=todo)

class UpdateTodoMutation(graphene.Mutation):
    """Mutation for updating an existing Todo."""
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        description = graphene.String()
        completed = graphene.Boolean()

    todo = graphene.Field(TodoType)

    def mutate(self, info, id, **kwargs):
        """Update the specified Todo with the provided data."""
        try:
            todo = Todo.objects.get(id=id)
            for key, value in kwargs.items():
                setattr(todo, key, value)
            todo.save()
            return UpdateTodoMutation(todo=todo)
        except Todo.DoesNotExist:
            return None

class DeleteTodoMutation(graphene.Mutation):
    """Mutation for deleting an existing Todo."""
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        """Delete the specified Todo."""
        try:
            todo = Todo.objects.get(id=id)
            todo.delete()
            return DeleteTodoMutation(success=True)
        except Todo.DoesNotExist:
            return DeleteTodoMutation(success=False)
