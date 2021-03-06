from django.db import models
from dashboard.models import Student, User
from django.urls import reverse

class Tiaozhancup(models.Model):
    is_review_by_school = models.BooleanField('院审核', default=False, null=True)
    is_review_by_college = models.BooleanField('校审核', default=False, null=True)
    is_review_by_boss = models.BooleanField('专家审核', default=False, null=True)

    def get_absolute_url(self):
        return reverse('tiaozhancup:tiaozhancup')

        