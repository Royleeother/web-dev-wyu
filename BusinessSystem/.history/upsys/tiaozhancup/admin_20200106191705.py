from django.contrib import admin

# Register your models here.
from .models import Tiaozhancup
from .pool import Stage1_pool, Stage2_pool, Stage3_pool
# from .judge_list import judge_list

admin.site.register(Tiaozhancup)
admin.site.register(Stage1_pool)
admin.site.register(Stage2_pool)
admin.site.register(Stage3_pool)
# admin.site.register(judge_list)