from django.forms import ModelForm
from django import forms
from .models import Contest1


class Contest1Form(ModelForm):
    apply_department = forms.CharField(label='申请部门', 
                    widget=forms.TextInput(attrs={'placeholder': ''}))
    apply_time = forms.CharField(label='申请时间', 
                    widget=forms.TextInput(attrs={'placeholder': 'X年X月X日X时X分 至 X年X月X日X时X分'}))
    contact_info = forms.CharField(label='联系方式', 
                    widget=forms.TextInput(attrs={'placeholder': '手机或微信'}))
    applyer = forms.CharField(label='申请人姓名', 
                    widget=forms.TextInput(attrs={'placeholder': ''}))
    apply_place = forms.CharField(label='申请地点', 
                    widget=forms.TextInput(attrs={'placeholder': ''}))
    what_u_need_to_do = forms.CharField(label='活动用途', 
                    widget=forms.TextInput(attrs={'placeholder': '简短说明'}))
    equipment_u_want = forms.CharField(label='所需设备', 
                    widget=forms.TextInput(attrs={'placeholder': ''}))
    
    class Meta:
        model = Contest1
        fields = '__all__'
        # 这是在表单里定义好HTML了，爱情买卖
        # widgets = {
        #     'gg1': forms.TextInput(attrs={'class': 'form-control'}),
        #     'gg2': forms.TextInput(attrs={'class': 'form-control'}),
        #     'gg3': forms.TextInput(attrs={'class': 'form-control'}),
        #     'gg4': forms.TextInput(attrs={'class': 'form-control'}),
        # }

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