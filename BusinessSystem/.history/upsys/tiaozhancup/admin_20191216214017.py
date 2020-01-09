from django.contrib import admin

# Register your models here.
from .models import Tiaozhancup
from .pool import school_pool, college_pool, boss_pool
from .judge_list import judge_list

admin.site.register(Tiaozhancup)
admin.site.register(school_pool)
admin.site.register(college_pool)
admin.site.register(boss_pool)
admin.site.register(judge_list)