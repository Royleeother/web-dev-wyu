from django.db import models

class School_pool(models.Model):
    econ = models.CharField('经济管理学院', max_length=500, null=True)
    cs = models.CharField('智能制造学部', max_length=500, null=True)
    law = models.CharField('政法学院', max_length=500, null=True)
    lietra = models.CharField('文学院', max_length=500, null=True)
    fore = models.CharField('外国语学院', max_length=500, null=True)
    math = models.CharField('数学与计算科学学院', max_length=500, null=True)
    phys = models.CharField('应用物理与材料学院', max_length=500, null=True)
    civil = models.CharField('土木建筑学院', max_length=500, null=True)
    bio = models.CharField('生物科技与大健康学院', max_length=500, null=True)
    weave = models.CharField('纺织材料与工程学院', max_length=500, null=True)
    art = models.CharField('艺术学院', max_length=500, null=True)

    # school_pool = {
    #     '经济管理学院': ['obj'],
    #     '智能制造学部': ['obj'],
    #     '政法学院': [],
    #     '文学院': [],
    #     '外国语学院': [],
    #     '数学与计算科学学院': [],
    #     '应用物理与材料学院': [],
    #     '土木建筑学院': [],
    #     '生物科技与大健康学院': [],
    #     '纺织材料与工程学院': []
    # }
class College_pool(models.Model):
    college_pool = models.CharField('校池', max_length=700, null=True)
    # college_pool = [
    #     'obj',
    # ]
class Boss_pool(models.Model):
    boss_pool = models.CharField('专家池', max_length=700, null=True)
    
    # boss_pool = [
    #     'obj',
    # ]

