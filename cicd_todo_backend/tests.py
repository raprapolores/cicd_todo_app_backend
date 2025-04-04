from django.db import connections
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Todo
from django.utils import timezone

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

    def test_todo_default_values(self):
        """
        Test that the default values (completed, created_at, updated_at) are set correctly.
        """
        todo = self.todo  # This is the Todo we created in setUp

        # Check default completed value
        self.assertFalse(todo.completed)

        # Check that created_at is set and is a datetime
        self.assertIsInstance(todo.created_at, timezone.datetime)
        self.assertIsInstance(todo.updated_at, timezone.datetime)

        # Ensure created_at and updated_at are not the same (since updated_at should change)
        self.assertNotEqual(todo.created_at, todo.updated_at)

    def test_update_todo(self):
        """
        Test updating a Todo item.
        """
        todo = self.todo
        # Update the Todo object
        todo.completed = True
        todo.save()

        # Reload the object from the database
        updated_todo = Todo.objects.get(id=todo.id)

        # Check that the 'completed' field has been updated
        self.assertTrue(updated_todo.completed)

        # Ensure updated_at is now different (because it's automatically updated)
        self.assertNotEqual(todo.updated_at, updated_todo.updated_at)