from django import forms
from todo.models import Todo

class TodoForm(forms.Form):
    todo_item = forms.CharField(label='To do item', max_length=150)
