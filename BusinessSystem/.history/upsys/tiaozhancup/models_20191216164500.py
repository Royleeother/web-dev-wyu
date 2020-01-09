from django.db import models
from dashboard.models import Student, User
from django.urls import reverse

class Tiaozhancup(models.Model):

    def get_absolute_url(self):
        return reverse('tiaozhancup:tiaozhancup')

        