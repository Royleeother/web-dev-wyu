from django.db import models

class Stage1_pool(models.Model):
    college_pool = models.CharField('厅室审核池', max_length=700, null=True)


class Stage2_pool(models.Model):
    college_pool = models.CharField('校律委审核池', max_length=700, null=True)
    
    
class Stage3_pool(models.Model):
    boss_pool = models.CharField('团委审核池', max_length=700, null=True)
    
