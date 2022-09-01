from dataclasses import fields
from django.forms import ModelForm
from todoapp.models import todolist

class TodoForm(ModelForm):
    class Meta:
        model = todolist
        fields = ['list', 'done']