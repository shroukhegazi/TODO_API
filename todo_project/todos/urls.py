from django.urls import path
from todos.views import ListTodo, DetailTodo
urlpatterns = [
    path('details/<int:pk>/', DetailTodo.as_view()),
    path('list/', ListTodo.as_view()),
]
