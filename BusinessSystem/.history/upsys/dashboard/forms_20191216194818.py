from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction

from dashboard.models import Student, Teacher, User

class StudentSignUpForm(UserCreationForm):
    # studentID = forms.IntegerField()
    SID = forms.CharField(label='学号', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))
    gender = forms.CharField(label='性别', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))
    username = forms.CharField(label='用户名', 
                    widget=forms.TextInput(attrs={'placeholder': '用于登陆', 
                                            'class': 'form-control',
                                            }))
    CHOICES = (
        ('经济管理学院', '经济管理学院'),
        ('智能制造学部', '智能制造学部'),
        ('政法学院', '政法学院'),
        ('文学院', '文学院'), 
        ('外国语学院', '外国语学院'),
        ('数学与计算科学学院', '数学与计算科学学院'),
        ('应用物理与材料学院', '应用物理与材料学院'),
        ('土木建筑学院', '土木建筑学院'),
        ('生物科技与大健康学院', '生物科技与大健康学院'),
        ('纺织材料与工程学院', '纺织材料与工程学院'),
    ) 
                                           
    school = forms.ChoiceField(label='所属学院', choices=CHOICES, 
                   widget=forms.Select(attrs={'class': 'form-control',
                    }))

    # 每增加一个数据模型，就把名字输进easylist, 这样你的人生就很轻松了
    easylist = [
        'SID',
        'gender',
        'username'
        'school',
    ]

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        data = self.cleaned_data
        give_value_to_user(self.easylist, student, data)
        # 上面这个函数相当于这三行，为了复用
        # 一下很烦 ~ 不管了
        # for item in self.easylist:
        #     dd = data.get(item)
        #     setattr(student, item, dd)
        # setattr 相当于下面这行
        # student.SID = data.get('SID')
        # 结束烦恼
        student.save()
        print("SID in forms:", student.SID)
        return user

class TeacherSignUpForm(UserCreationForm):
    TID = forms.CharField(label='工号', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))
    department = forms.CharField(label='所属学院/部门', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))
    gender = forms.CharField()
    username = forms.CharField()
    # 记得加到easylist哦，奥利给！！！
    easylist = [
        'TID',
        'gender',
        'department',
        'username',
    ]

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        data = self.cleaned_data
        # 一下很烦 ~ 不管了
        give_value_to_user(self.easylist, teacher, data)
        # 结束烦恼
        teacher.save()
        print("TID in forms:", teacher.TID)
        return user

# class StudentInfoUpdateForm(UserChangeForm):
#     return 

# HELPER FUNCTIONS

# 实现自动保存表单内容
def give_value_to_user(easylist, user, cleaned_data):
    """
    easylist, user, cleaned_data
    """
    for item in easylist:
        dd = cleaned_data.get(item, '')
        setattr(user, item, dd)