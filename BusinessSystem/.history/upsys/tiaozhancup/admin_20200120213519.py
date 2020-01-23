from django.contrib import admin

# Register your models here.
from .models import Tiaozhancup
from .pool import School_pool, College_pool, Boss_pool, Temp_pool
# from .judge_list import judge_list

admin.site.register(Tiaozhancup)
admin.site.register(School_pool)
admin.site.register(College_pool)
admin.site.register(Boss_pool)
admin.site.register(Temp_pool)
# admin.site.register(judge_list)