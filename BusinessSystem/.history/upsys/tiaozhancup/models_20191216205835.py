from django.db import models
from dashboard.models import Student, User
from django.urls import reverse

class Tiaozhancup(models.Model):
    is_review_by_schoole = models.BooleanField('院审核', default=False, null=True)

    def get_absolute_url(self):
        return reverse('tiaozhancup:tiaozhancup')

        