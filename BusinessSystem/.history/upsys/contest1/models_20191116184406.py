from django.db import models
from dashboard.models import Student

class Contest1(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='content1')
    gg1 = models.CharField(max_length=100)
    gg2 = models.CharField(max_length=100)
    gg3 = models.CharField(max_length=100)
    gg4 = models.CharField(max_length=100)

    def __str__(self):
        return 'FORM {}'.format(self.student.username)