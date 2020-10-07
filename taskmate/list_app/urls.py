from list_app import views
from django.urls import path

urlpatterns = [
    path("/", views.todo_list, name="todolist"),
]
