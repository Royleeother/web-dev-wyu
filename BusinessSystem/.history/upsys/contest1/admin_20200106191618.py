from django.contrib import admin

# Register your models here.
from .models import Contest1
from .pool import School_pool, College_pool, Boss_pool

admin.site.register(Contest1)
admin.site.register(Contest1)