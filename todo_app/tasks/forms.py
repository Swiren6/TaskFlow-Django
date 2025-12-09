from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter task title...',
                'autofocus': True,
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Add a description (optional)...',
                'rows': 4,
            }),
            'priority': forms.Select(attrs={
                'class': 'form-select',
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date',
            }),
        }
        labels = {
            'title': 'Task Title',
            'description': 'Description',
            'priority': 'Priority Level',
            'due_date': 'Due Date',
        }
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title:
            title = title.strip()
            if len(title) < 2:
                raise forms.ValidationError('Title must be at least 2 characters long.')
        return title