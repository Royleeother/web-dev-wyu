from django.db import models

class stage1_pool(models.Model):
    college_pool = models.CharField('厅室审核池', max_length=700, null=True)


class stage2_pool(models.Model):
    college_pool = models.CharField('校律委审核池', max_length=700, null=True)
    
    
class stage3_pool(models.Model):
    boss_pool = models.CharField('团委审核池', max_length=700, null=True)
    
