from django.forms import ModelForm
from django import forms
from .models import Content1


class Content1Form(ModelForm):
    gg1 = forms.CharField()
    gg2 = forms.CharField()
    gg3 = forms.CharField()
    gg4 = forms.CharField()

    class Meta:
        model = Subject
        fields = ['gg1', 'gg2', 'gg3', 'gg4']
