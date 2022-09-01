from django.contrib import admin
from django.urls import path
from todoapp import views
urlpatterns = [
    path('', views.todo_list, name="todo_list"),
    path('delete_list/<id>', views.delete_list, name="delete_list"),
    path('update_list/<id>', views.update_list, name="update_list"),
    path('complete_list/<id>', views.complete_list, name="complete_list"),
    path('pending_list/<id>', views.pending_list, name="pending_list"),
]