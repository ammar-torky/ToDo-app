from django.forms import ModelForm
from .models import Todo

class AddNewTodo(ModelForm):  # Class names should follow PascalCase convention
    class Meta:
        model = Todo
        fields = ['text']
