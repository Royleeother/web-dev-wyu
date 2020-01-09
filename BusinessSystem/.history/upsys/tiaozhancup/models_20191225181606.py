from django.db import models
from dashboard.models import Student, User
from django.urls import reverse

class Tiaozhancup(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='tiaozhancup')

    overall_type = models.CharField('大类', max_length=50, null=True)
    overall_type = models.CharField('申报种类', max_length=50, null=True)
    school = models.CharField('高校', max_length=50, null=True)
    top_academic_level = models.CharField('最高学历', max_length=50, null=True)
    #申报人信息
    applyer = models.CharField('申报人姓名', max_length=50, null=True)
    gender = models.CharField('性别', max_length=50, null=True)
    birth = models.CharField('生日', max_length=50, null=True)
    id_type = models.CharField('证件类型', max_length=50, null=True)
    id_number = models.CharField('证件号码', max_length=50, null=True)
    major = models.CharField('专业', max_length=50, null=True)
    grade = models.CharField('年级', max_length=50, null=True)
    entry_year = models.CharField('入学年份', max_length=50, null=True)
    school_id = models.CharField('学号', max_length=50, null=True)
    school_type = models.CharField('学制', max_length=50, null=True)
    essay_title = models.CharField('毕业论文题目', max_length=100, null=True)
    address_whole = models.CharField('通讯地址', max_length=100, null=True)
    postal_code = models.CharField('邮政编码', max_length=50, null=True)
    dorm_phone = models.CharField('学校宿舍电话', max_length=50, null=True)
    address_usually = models.CharField('常住通讯地址', max_length=100, null=True)
    school_type = models.CharField('学制', max_length=50, null=True)
    home_number = models.CharField('家庭电话', max_length=50, null=True)
    mobile_number = models.CharField('移动电话', max_length=50, null=True)
    wechat_number = models.CharField('微信号', max_length=50, null=True)
    #推荐人填报信息
    recommend_name = models.CharField('推荐人姓名', max_length=50, null=True)
    recommend_gender = models.CharField('推荐人姓别', max_length=50, null=True)
    recommend_age = models.CharField('推荐人年龄', max_length=50, null=True)
    recommend_title = models.CharField('推荐人职称', max_length=50, null=True)
    recommend_office = models.CharField('推荐人工作单位', max_length=50, null=True)
    recommend_address = models.CharField('推荐人通讯地址', max_length=100, null=True)
    recommend_postal_code = models.CharField('推荐人邮政编码', max_length=50, null=True)
    recommend_mobile_number = models.CharField('推荐人电话号码', max_length=50, null=True)
    recommend_home_number = models.CharField('推荐人住宅号码', max_length=50, null=True)
    recommend_fact_check = models.CharField('推荐人请对申报者申报情况的真实性作出阐述', max_length=50, null=True)
    recommend_comment = models.CharField('推荐人请对作品的意义、技术水平、适用范围及推广前景作出评价', max_length=100, null=True)
    recommend_other_comment = models.CharField('推荐人其他说明', max_length=50, null=True)
    #作品信息
    project_name = models.CharField('项目名称', max_length=50, null=True)
    class_one = models.CharField('小类', max_length=50, null=True)
    class_three = models.CharField('三级分类', max_length=50, null=True)
    class_four = models.CharField('四级分类', max_length=50, null=True)
    detail_intro = models.CharField('详细介绍', max_length=500, null=True)
    technique_point = models.CharField('作品设计、发明的目的和基本思路、创新点、技术关键和主要技术目标：', max_length=500, null=True)
    # 审核状态
    is_review_by_school = models.BooleanField('院审核', default=False, null=True)
    is_review_by_college = models.BooleanField('校审核', default=False, null=True)
    is_review_by_boss = models.BooleanField('专家审核', default=False, null=True)
    #
    school_staff_give = models.CharField(max_length=500, null=True, default=str({}),)
    college_staff_give = models.CharField(max_length=500, null=True, default=str({}),)
    boss_staff_give = models.CharField(max_length=500, null=True, default=str({}),)
    #
    is_pass = models.BooleanField('is_pass', default=False, null=True)
    is_fail = models.BooleanField('is_fail', default=False, null=True)
    is_reviewing = models.BooleanField('is_reviewing', default=True, null=True)


    def get_absolute_url(self):
        return reverse('tiaozhancup:tiaozhancup')

