from rest_framework.test import APITestCase
from django.shortcuts import render
from .models import Todo
class TodoTests(APITestCase):
    def todo_list(request):
        todos = Todo.objects.all()
        return render(request, 'todo_list.html', {'todos': todos})