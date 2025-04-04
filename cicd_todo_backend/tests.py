from django.db import connections
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Todo

class TodoApiTests(APITestCase):

    @classmethod
    def tearDownClass(self):
        connections.close_all()
    def setUp(self):
        """
        Set up method called before each test.
        Here we create a sample Todo object.
        """
        self.todo = Todo.objects.create(
            title="Test Todo",
            content="This is a test todo item."
        )
    def test_todo_creation(self):
        """
        Test that the Todo object is created correctly in the database.
        """
        # Retrieve the Todo object we created
        todo = Todo.objects.get(title="Test Todo")

        # Check that the title and content are correct
        self.assertEqual(todo.title, "Test Todo")
        self.assertEqual(todo.content, "This is a test todo item.")
        self.assertFalse(todo.completed)  # Default value should be False
