from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'complete']
        widgets = {'description': forms.Textarea(attrs={'cols': 80})}