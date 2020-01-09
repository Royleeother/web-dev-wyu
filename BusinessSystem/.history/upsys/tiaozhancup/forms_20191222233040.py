from django.forms import ModelForm
from django import forms
from .models import Tiaozhancup

class TiaozhancupForm(ModelForm):
    test = forms.CharField(label='测试', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))
    class Meta:
        model = Tiaozhancup
        # fields = '__all__'
        fields = [
            'test'
            # 'apply_department',
            # 'apply_time',
            # 'contact_info',
            # 'applyer',
            # 'apply_place',
            # 'what_u_need_to_do',
            # 'equipment_u_want',
        ]

class Tiaozhancup_for_review(forms.Form):
    decision = forms.BooleanField(label='是否审核通过',required=False,
                                        widget=forms.RadioSelect(
                                        choices=YES_NO, 
                                        attrs={'class': 'form-control', 
                                                'required':True,
                            }))
    comment = forms.CharField(label='留言', 
                    widget=forms.TextInput(
                                    attrs={'class': 'form-control',
                                    'placeholder': '简短说明',
                                }))

        
    