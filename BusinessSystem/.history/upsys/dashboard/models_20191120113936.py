from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_student = models.BooleanField('student status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=50, blank=True, null=True) #这个是为了能在admin能用，就当他是真实姓名吧，管它呢
    SID = models.CharField(max_length=50, blank=True, null=True) 
    gender = models.CharField(max_length=50, blank=True, null=True)
    contest = models.CharField(max_length=500, blank=True, null=True)

class Teacher(models.Model):
    really_a_teacher = models.BooleanField('真的是老师吗 ?', default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    TID = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    authorization_for_contest = models.CharField(max_length=500, blank=True, null=True)

# {% if 'Contest1' not in eval(user.student.contest) %}
# {% else %}
# {% endif %}