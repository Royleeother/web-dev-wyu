from django.db import models
from dashboard.models import Student, User
from django.urls import reverse

class Contest1(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='content1')
    apply_department = models.CharField(max_length=100, null=True)
    apply_time = models.CharField(max_length=100, null=True)
    applyer = models.CharField(max_length=100, null=True)
    contact_info = models.CharField(max_length=100, null=True)
    apply_place = models.CharField(max_length=100, null=True)
    what_u_need_to_do = models.CharField(max_length=500, null=True)
    equipment_u_want = models.CharField(max_length=100, null=True)

    guiding_unit_opnion = models.CharField(max_length=100, null=True)
    discipline_unit_opnion = models.CharField(max_length=100, null=True)
    ccyl_opnion = models.CharField(max_length=100, null=True)

    have_registered = models.BooleanField('have_registered', default=False, null=True)
    is_pass = models.BooleanField('is_pass', default=False, null=True)
    is_fail = models.BooleanField('is_fail', default=False, null=True)
    is_reviewing = models.BooleanField('is_reviewing', default=True, null=True)

    def __str__(self):
        return 'FORM ({})'.format(self.student.username)

    def get_absolute_url(self):
        return reverse('contest1:contest1')
