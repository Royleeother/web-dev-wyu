from django.forms import ModelForm
from django import forms
from .models import Contest1


class Contest1Form(ModelForm):
    apply_department = forms.CharField(label='申请部门', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))
    apply_time = forms.CharField(label='申请时间', 
                    widget=forms.TextInput(attrs={'placeholder': 'X年X月X日X时X分 至 X年X月X日X时X分' ,
                                            'class': 'form-control',
                                            }))
    contact_info = forms.CharField(label='联系方式', 
                    widget=forms.TextInput(attrs={'placeholder': '手机或微信', 
                                            'class': 'form-control',
                                            }))
    applyer = forms.CharField(label='申请人姓名', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))
    CHOICES = (('Option 1', '舞厅'),('Option 2', '多功能厅'),('Option 3', '报告厅'),)
    apply_place = forms.ChoiceField(label='申请地点', choices=CHOICES, 
                    widget=forms.Select(attrs={'class': 'form-control',
                                            }))
    what_u_need_to_do = forms.CharField(label='活动用途', 
                    widget=forms.TextInput(attrs={'placeholder': '简短说明', 
                                            'class': 'form-control',
                                            }))
    equipment_u_want = forms.CharField(label='所需设备', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))
    
    class Meta:
        model = Contest1
        # fields = '__all__'
        fields = [
            'apply_department',
            'apply_time',
            'contact_info',
            'applyer',
            'apply_place',
            'what_u_need_to_do',
            'equipment_u_want',
        ]
        # 这是在表单里定义好HTML了，爱情买卖
        # widgets = {
        #     'gg1': forms.TextInput(attrs={'class': 'form-control'}),
        #     'gg2': forms.TextInput(attrs={'class': 'form-control'}),
        #     'gg3': forms.TextInput(attrs={'class': 'form-control'}),
        #     'gg4': forms.TextInput(attrs={'class': 'form-control'}),
        # }

class Contest1_for_review(ModelForm, review_type):
    ### 改成 Contest1_for_review
    class Meta(review_type):
        def __init__(self, review_type):
            self.review_type = review_type

        model = Contest1

        decision = review_type + '_decision'
        comment = review_type +'comment'

        fields = [
            decision,
            comment,
        ]
        labels = {
            decision: "是否审核通过",
            comment: '留言',
        }
        YES_NO = ((True, '是'), (False, '否'))
        widgets = {
            decision: forms.RadioSelect(
                                        choices=YES_NO, 
                                        attrs={'class': 'form-control', 
                                                    'required':True,
                                                    }),
            comment: forms.TextInput(
                                        attrs={'class': 'form-control',
                                        'placeholder': '简短说明',
                                        
                                    }),
        }

    def get_absolute_url(self):
        return reverse('contest1:contest1_review')