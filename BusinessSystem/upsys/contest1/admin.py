from django.contrib import admin

# Register your models here.
from .models import Contest1
from .pool import Stage1_pool, Stage2_pool, Stage3_pool

admin.site.register(Contest1)
#
admin.site.register(Stage1_pool)
admin.site.register(Stage2_pool)
admin.site.register(Stage3_pool)