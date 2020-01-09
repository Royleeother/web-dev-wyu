from django.contrib import admin

# Register your models here.
from .models import User, Student, Teacher

admin.site.register(User)