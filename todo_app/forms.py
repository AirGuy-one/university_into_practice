from django import forms
from django.contrib.auth.models import User

from .models import Todo


class TodoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields['user'].initial = User.objects.last()

    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'введите назваие'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'введите описание'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'title': '',
            'description': '',
            'completed': 'сделано',
            'user': '',
        }
