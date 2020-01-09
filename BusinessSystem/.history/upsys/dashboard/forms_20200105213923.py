from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from django.contrib.auth.forms import PasswordResetForm
from dashboard.models import Student, Teacher, User

CHOICES_DEPARTMENT = (
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
        ('艺术学院', '艺术学院'),
    )
CHOICES_GENDER = (
    ('男', '男'),
    ('女', '女')
)

class StudentSignUpForm(UserCreationForm):
    # studentID = forms.IntegerField()
    SID = forms.CharField(label='学号', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))
    gender = forms.ChoiceField(label='性别', choices=CHOICES_GENDER, 
                    widget=forms.Select(attrs={
                                            'class': 'form-control',
                                            }))
    username = forms.CharField(label='用户名', 
                    widget=forms.TextInput(attrs={'placeholder': '用于登陆', 
                                            'class': 'form-control',
                                            })) 
    email = forms.CharField(label='邮箱', 
                    widget=forms.TextInput(attrs={'placeholder': '用于处理忘记密码情况', 
                                            'class': 'form-control',
                                            }))                                       
    school = forms.ChoiceField(label='所属学院', choices=CHOICES_DEPARTMENT, 
                   widget=forms.Select(attrs={'class': 'form-control',
                    }))
    phone_number = forms.CharField(label='手机号码', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))   

    # 每增加一个数据模型，就把名字输进easylist, 这样你的人生就很轻松了
    easylist = [
        'SID',
        'gender',
        'username',
        'school',
        'email',
        'phone_number',
    ]

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        #
        data = self.cleaned_data
        setattr(user, 'email', data['email'])
        user.save()
        student = Student.objects.create(user=user)
        give_value_to_user(self.easylist, student, data)
        # 上面这个函数相当于这三行，为了复用
        # 一下很烦 ~ 不管了
        # for item in self.easylist:
        #     dd = data.get(item)
        #     setattr(student, item, dd)
        # setattr 相当于下面这行
        # student.SID = data.get('SID')
        # 结束烦恼
        print("SID in forms:", student.SID)
        return user

class TeacherSignUpForm(UserCreationForm):
    TID = forms.CharField(label='工号', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))
    department = forms.ChoiceField(label='所属学院/部门', choices=CHOICES_DEPARTMENT, 
                   widget=forms.Select(attrs={'class': 'form-control',
                    }))
    gender = forms.CharField(label='性别', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))
    username = forms.CharField(label='用户名', 
                    widget=forms.TextInput(attrs={'placeholder': '用于登陆', 
                                            'class': 'form-control',
                                            }))
    email = forms.CharField(label='邮箱', 
                    widget=forms.TextInput(attrs={'placeholder': '用于处理忘记密码情况', 
                                            'class': 'form-control',
                                            }))
    phone_number = forms.CharField(label='手机号码', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))                                                                                    
    # 记得加到easylist哦，奥利给！！！
    easylist = [
        'TID',
        'gender',
        'department',
        'username',
        'email',
        'phone_number',
    ]

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        #
        data = self.cleaned_data
        setattr(user, 'email', data['email'])
        user.save()
        teacher = Teacher.objects.create(user=user)
        # 一下很烦 ~ 不管了
        give_value_to_user(self.easylist, teacher, data)
        # 结束烦恼
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
        print("没有 item?:", item)
        dd = cleaned_data.get(item, '')
        print("难道是dd的问题？：", dd)
        setattr(user, item, dd)
    user.save()

class Password_first_step(PasswordResetForm):
    ID = forms.CharField(label='学号', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))
    class Meta:
        model = User
        fields = ("ID")