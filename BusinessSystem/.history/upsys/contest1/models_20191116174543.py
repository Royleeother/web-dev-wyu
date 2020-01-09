from django.db import models
from dashboard.models import Student

class Content1(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='content1')
    hjhj = models.CharField(max_length=100)
    jgkd = models.CharField(max_length=100)
    hfguh = models.CharField(max_length=100)
    ighsdghs = models.CharField(max_length=100)

    def __str__(self):
        return 'FORM {}'.format(self.user.username)