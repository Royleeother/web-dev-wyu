from django.db import models
from dashboard.models import Student, User
from django.urls import reverse

class Contest1(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='content1')
    gg1 = models.CharField(max_length=100)
    gg2 = models.CharField(max_length=100)
    gg3 = models.CharField(max_length=100)
    gg4 = models.CharField(max_length=100)

    have_registered = models.BooleanField('have_registered', default=False)
    is_pass = models.BooleanField('is_pass', default=False)
    is_fail = models.BooleanField('is_fail', default=False)
    is_reviewing = models.BooleanField('is_reviewing', default=False)

    def __str__(self):
        return 'FORM {}'.format(self.student.username)

    def get_absolute_url(self):
        return reverse('contest1:contest1')
