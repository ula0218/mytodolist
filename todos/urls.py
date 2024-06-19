from django.urls import path
from .views import (
    ToDoListView, 
    ToDoCreateView, 
    ToDoUpdateView, 
    ToDoDeleteView
)

app_name = 'todos'

urlpatterns = [
    path("", ToDoListView.as_view(), name='list'),
    path("create/", ToDoCreateView.as_view(), name='create'),
    path("<int:pk>/update/", ToDoUpdateView.as_view(), name='update'),
    path("<int:pk>/delete/", ToDoDeleteView.as_view(), name='delete'),
]