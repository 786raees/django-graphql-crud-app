# Django GraphQL CRUD App

This project is a Django-based application that implements a CRUD (Create, Read, Update, Delete) functionality for managing todos using GraphQL. It provides an interface for creating, retrieving, updating, and deleting todo items.🚀📝

## Prerequisites

Before running the Django GraphQL CRUD App, ensure that you have the following prerequisites installed on your machine:

- Python (version 3.8 or higher)
- Django (version 3.2 or higher)

## Installation

To set up and run the Django GraphQL CRUD App, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/786raees/django-graphql-crud-app.git
   ```

2. Navigate to the project directory:

   ```
   cd django-graphql-crud-app
   ```

3. Create a virtual environment (optional but recommended):

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Apply database migrations:

   ```
   python manage.py migrate
   ```

6. Start the development server:

   ```
   python manage.py runserver
   ```

7. Open your web browser and access the application at `http://localhost:8000/graphql`.

## Usage

The Django GraphQL CRUD App provides a GraphQL endpoint for performing CRUD operations on todos. The available operations include:

- Querying all todos
- Creating a new todo
- Updating an existing todo
- Deleting a todo

To interact with the GraphQL API, you can use tools like GraphiQL or any GraphQL client. The GraphQL endpoint is located at `http://localhost:8000/graphql`.

The following GraphQL schema defines the available queries and mutations:

```graphql
type Todo {
  id: ID!
  title: String!
  description: String!
  completed: Boolean!
}

type Query {
  todos: [Todo!]!
}

type Mutation {
  createTodo(title: String!, description: String!): Todo
  updateTodo(id: ID!, title: String, description: String, completed: Boolean): Todo
  deleteTodo(id: ID!): Boolean
}
```

You can use these schema definitions to construct GraphQL queries and mutations to interact with the API.

## Examples

Here are some examples of GraphQL queries and mutations that can be used with the Django GraphQL CRUD App:

- Query all todos:

  ```graphql
  query {
    todos {
      id
      title
      description
      completed
    }
  }
  ```

- Create a new todo:

  ```graphql
  mutation {
    createTodo(title: "New Todo", description: "This is a new todo") {
      id
      title
      description
      completed
    }
  }
  ```

- Update an existing todo:

  ```graphql
  mutation {
    updateTodo(id: "123", title: "Updated Todo") {
      id
      title
      description
      completed
    }
  }
  ```

- Delete a todo:

  ```graphql
  mutation {
    deleteTodo(id: "123")
  }
  ```

Feel free to customize the queries and mutations according to your requirements.

## Contributing

Contributions to the

 Django GraphQL CRUD App are welcome. If you find a bug or have a suggestion for improvement, please open an issue or submit a pull request on the repository.