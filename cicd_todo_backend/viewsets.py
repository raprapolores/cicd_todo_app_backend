from rest_framework import viewsets

from cicd_todo_backend.models import Todo
from cicd_todo_backend.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer