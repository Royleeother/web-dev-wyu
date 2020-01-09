from django.forms import ModelForm
from django import forms
from .models import Content1


class Content1Form(ModelForm):
    username = forms.CharField()
    username = forms.CharField()
    username = forms.CharField()
    username = forms.CharField()
    
    class Meta:
        model = Subject
        fields = ['subject_name', 'subject_code']
