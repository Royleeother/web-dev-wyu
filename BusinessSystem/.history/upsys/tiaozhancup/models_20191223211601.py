from django.db import models
from dashboard.models import Student, User
from django.urls import reverse

class Tiaozhancup(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='tiaozhancup')
    test = models.CharField(max_length=100, null=True)

    # overall_type = models.CharField('大类', max_length=50, null=True)
    # overall_type = models.CharField('申报种类', max_length=50, null=True)
    # school = models.CharField('高校', max_length=50, null=True)
    # top_academic_level = models.CharField('最高学历', max_length=50, null=True)
    #

    # 审核状态
    is_review_by_school = models.BooleanField('院审核', default=False, null=True)
    is_review_by_college = models.BooleanField('校审核', default=False, null=True)
    is_review_by_boss = models.BooleanField('专家审核', default=False, null=True)
    #
    school_staff_give = models.CharField(max_length=500, null=True, default=str({}),)
    college_staff_give = models.CharField(max_length=500, null=True, default=str({}),)
    boss_staff_give = models.CharField(max_length=500, null=True, default=str({}),)
    #
    is_pass = models.BooleanField('is_pass', default=False, null=True)
    is_fail = models.BooleanField('is_fail', default=False, null=True)
    is_reviewing = models.BooleanField('is_reviewing', default=True, null=True)


    def get_absolute_url(self):
        return reverse('tiaozhancup:tiaozhancup')

