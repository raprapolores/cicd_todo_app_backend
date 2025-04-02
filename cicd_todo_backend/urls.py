
from django.urls import path
from rest_framework import routers

from cicd_todo_backend.views import RegisterView, LoginView, LogoutView, UserView
from cicd_todo_backend.viewsets import TodoViewSet

router = routers.DefaultRouter()
router.register('todo', TodoViewSet, basename='todos')
urlpatterns = router.urls
urlpatterns.append(path('register/', RegisterView.as_view(), name='register'))
urlpatterns.append(path('login/', LoginView.as_view(), name='login'))
urlpatterns.append(path('logout/', LogoutView.as_view(), name='logout'))
