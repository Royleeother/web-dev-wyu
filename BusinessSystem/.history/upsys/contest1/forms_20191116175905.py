from django.forms import ModelForm
from django import forms
from .models import Content1

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_name', 'subject_code']
        widgets = {
            'subject_name': forms.TextInput(attrs={'class': 'form-control'}),
            'subject_code':  forms.NumberInput(attrs={'class': 'form-control'}),
        }

class Content1Form(ModelForm)
