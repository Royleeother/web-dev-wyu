from django.forms import ModelForm
from django import forms
from .models import Contest1


class Contest1Form(ModelForm):
    gg1 = forms.CharField()
    gg2 = forms.CharField()
    gg3 = forms.CharField()
    gg4 = forms.CharField()

    class Meta:
        model = Contest1
        fields = ['gg1', 'gg2', 'gg3', 'gg4']
        # 这是在表单里定义好HTML了，爱情买卖
        widgets = {
            'gg1': forms.TextInput(attrs={'class': 'form-control'}),
            'gg2': forms.TextInput(attrs={'class': 'form-control'}),
            'gg3': forms.TextInput(attrs={'class': 'form-control'}),
            'gg4': forms.TextInput(attrs={'class': 'form-control'}),
        }

class Contest1ReviewForm(ModelForm):
    gg1 = forms.CharField()
    gg2 = forms.CharField()
    gg3 = forms.CharField()
    gg4 = forms.CharField()

    class Meta:
        model = Contest1
        fields = ['gg1', 'gg2', 'gg3', 'gg4']

    def get_absolute_url(self):
        return reverse('contest1:contest1')