from django.forms import ModelForm
from django import forms
from .models import Tiaozhancup

class TiaozhancupForm(ModelForm):

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