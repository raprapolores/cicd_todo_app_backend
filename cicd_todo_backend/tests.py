from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Todo

class TodoTests(APITestCase):
    def setUp(self):
        # Setup code: create some test data
        self.todo_data = {'title': 'Test Todo', 'content': 'Test Description', 'completed': False}
        self.todo = Todo.objects.create(**self.todo_data)
        self.url = reverse('todo-list')  # Assuming you use `todo-list` for your list view
        self.todo_detail_url = reverse('todo-detail', args=[self.todo.pk])  # Detail view URL

    def test_create_todo(self):
        """
        Ensure we can create a new todo item.
        """
        response = self.client.post(self.url, self.todo_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.todo_data['title'])
        self.assertEqual(response.data['content'], self.todo_data['content'])