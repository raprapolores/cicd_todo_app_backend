from django.db import models

# Create your models here
# Add model to create todo item,update todo item
class Todo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
