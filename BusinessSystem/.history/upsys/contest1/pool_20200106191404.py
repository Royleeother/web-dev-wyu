from django.db import models

class Stage1_pool(models.Model):
    stage1_pool = models.CharField('厅室审核池', max_length=700, null=True)

    def __str__(self):
        return 'FORM ({})'.format(stage1_pool)
    

class Stage2_pool(models.Model):
    stage2_pool = models.CharField('校律委审核池', max_length=700, null=True)
    
    def __str__(self):
        return 'FORM ({})'.format(stage2_pool)
    
    
class Stage3_pool(models.Model):
    stage3_pool = models.CharField('团委审核池', max_length=700, null=True)
    
    def __str__(self):
        return 'FORM ({})'.format(stage3_pool)
