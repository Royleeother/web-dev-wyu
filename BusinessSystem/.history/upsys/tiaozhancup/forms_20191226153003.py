from django.forms import ModelForm
from django import forms
from .models import Tiaozhancup

class TiaozhancupForm(ModelForm):
    # test = forms.CharField(label='测试', 
    #                 widget=forms.TextInput(attrs={'placeholder': '', 
    #                                         'class': 'form-control',
    #                                         }))
    CHOICES = (('自然科学类', '自然科学类'),
                ('哲学社科类', '哲学社科类'),
                ('科技发明制作A类', '科技发明制作A类'),
                ('科技发明制作B类', '科技发明制作B类'),)
    overall_type = forms.ChoiceField(label='大类', choices=CHOICES, 
                    widget=forms.Select(attrs={'class': 'form-control',
                                            }))
    shenbaozlei =   (('已创业', '已创业'),
                ('未创业', '未创业'),
                )
    request_type =  forms.ChoiceField(label='', choices=shenbaozlei, 
                    widget=forms.Select(attrs={'class': 'form-control',
                                            }))  
    school = forms.CharField(label='高校', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))
    top_academic =   (('博士', '博士'),
                ('硕士研究生', '硕士研究生'),
                ('本科', '本科'),
                ('高中', '高中'),
                ('初中', '初中'),
                ('小学', '小学'),
                )
    top_academic_level =  forms.ChoiceField(label='大类', choices=top_academic, 
                    widget=forms.Select(attrs={'class': 'form-control',
                                            })) 
    applyer = forms.CharField(label='姓名', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))
    gender_mn =   (('男', '男'),
                ('女', '女'),               
                )
    gender =  forms.ChoiceField(label='性别', choices=gender_mn, 
                    widget=forms.Select(attrs={'class': 'form-control',
                                            })) 
    birth = forms.CharField(label='生日', 
                    widget=forms.TextInput(attrs={'placeholder': '格式：1999-07-24', 
                                            'class': 'form-control',
                                            }))
    
    id_typeit =   (('居民身份证', '居民身份证'),
                ('护照', '护照'), 
                ('港澳身份证', '港澳身份证'),              
                )
    id_type =  forms.ChoiceField(label='证件类型', choices=id_typeit, 
                    widget=forms.Select(attrs={'class': 'form-control',
                                            }))
    id_number = forms.CharField(label='证件号码', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))

    major = forms.CharField(label='专业', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))


    grade = forms.CharField(label='年级', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))

    entry_year = forms.CharField(label='入学年份', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))


    school_id = forms.CharField(label='学号', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))

    school_type = forms.CharField(label='学制', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))

    gradua_paper_title = forms.CharField(label='毕业论文题目', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))

    address_whole = forms.CharField(label='通讯地址', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))

    postal_code = forms.CharField(label='邮政编码', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))

    dorm_phone = forms.CharField(label='学校宿舍电话', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))


    address_usually = forms.CharField(label='常住通讯地址', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))

    postal_code_user = forms.CharField(label='常住邮政编码', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))
    home_number = forms.CharField(label='家庭电话', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))

    mobile_number = forms.CharField(label='移动电话', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))

    wechat_number = forms.CharField(label='微信号', 
                        widget=forms.TextInput(attrs={'placeholder': '', 
                                                'class': 'form-control',
                                                }))

    #推荐人填报信息

    recommend_name = forms.CharField(label='推荐人姓名', 
                        widget=forms.TextInput(attrs={'placeholder': '', 
                                                'class': 'form-control',
                                                }))

    recommend_gender = forms.CharField(label='推荐人姓别', 
                        widget=forms.TextInput(attrs={'placeholder': '', 
                                                'class': 'form-control',
                                                }))

    recommend_age = forms.CharField(label='推荐人年龄', 
                        widget=forms.TextInput(attrs={'placeholder': '', 
                                                'class': 'form-control',
                                                }))


    recommend_title = forms.CharField(label='推荐人职称', 
                        widget=forms.TextInput(attrs={'placeholder': '', 
                                                'class': 'form-control',
                                                }))

    recommend_office = forms.CharField(label='推荐人工作单位', 
                        widget=forms.TextInput(attrs={'placeholder': '', 
                                                'class': 'form-control',
                                                }))

    recommend_address = forms.CharField(label='推荐人通讯地址', 
                        widget=forms.TextInput(attrs={'placeholder': '', 
                                                'class': 'form-control',
                                                }))

    recommend_postal_code = forms.CharField(label='推荐人邮政编码', 
                        widget=forms.TextInput(attrs={'placeholder': '', 
                                                'class': 'form-control',
                                                }))

    recommend_mobile_number = forms.CharField(label='推荐人电话号码', 
                        widget=forms.TextInput(attrs={'placeholder': '', 
                                                'class': 'form-control',
                                                }))

    recommend_home_number = forms.CharField(label='推荐人住宅号码', 
                        widget=forms.TextInput(attrs={'placeholder': '', 
                                                'class': 'form-control',
                                                }))

    recommend_fact_check = forms.CharField(label='推荐人请对申报者申报情况的真实性作出阐述', 
                        widget=forms.TextInput(attrs={'placeholder': '500字内', 
                                                'class': 'form-control',
                                                }))

    recommend_comment = forms.CharField(label='推荐人请对作品的意义、技术水平、适用范围及推广前景作出评价', 
                        widget=forms.TextInput(attrs={'placeholder': '1000字内', 
                                                'class': 'form-control',
                                                }))


    recommend_other_comment = forms.CharField(label='推荐人其他说明', 
                        widget=forms.TextInput(attrs={'placeholder': '500字内', 
                                                'class': 'form-control',
                                                }))

#作品信息


    project_name = forms.CharField(label='项目名称', 
                        widget=forms.TextInput(attrs={'placeholder': '', 
                                                'class': 'form-control',
                                                }))

    id_typeit =   (('机械与控制', '机械与控制'),
                ('信息技术', '信息技术'), 
                ('港澳身份证', '港澳身份证'),  
                ('数理', '数理'), 
                ('生命科学', '生命科学'), 
                ('能源化工', '能源化工'), 
                ('哲学', '哲学'), 
                ('经济', '经济'), 
                ('社会', '社会'),  
                ('法律', '法律'), 
                ('教育', '教育'),  
                ('管理', '管理'), 
                ('生物医药', '生物医药'), 
                ('电子信息', '电子信息'), 
                ('机械能源', '机械能源'), 
                ('服务咨询', '服务咨询'), 
                ('农林畜牧食品', '农林畜牧食品'),   
                ('化工环境', '化工环境'), 
                ('材料', '材料'),              
                )
    class_one =  forms.ChoiceField(label='小类', choices=id_typeit, 
                    widget=forms.Select(attrs={'class': 'form-control',
                                            }))

    

    class_three = forms.CharField(label='三级分类', 
                        widget=forms.TextInput(attrs={'placeholder': '', 
                                                'class': 'form-control',
                                                }))

    class_four = forms.CharField(label='四级分类', 
                        widget=forms.TextInput(attrs={'placeholder': '', 
                                                'class': 'form-control',
                                                }))

    short_intro = forms.CharField(label='简介', 
                        widget=forms.TextInput(attrs={'placeholder': '500字内', 
                                                'class': 'form-control',
                                                }))

    detail_intro = forms.CharField(label='详细介绍', 
                        widget=forms.TextInput(attrs={'placeholder': '2000字内', 
                                                'class': 'form-control',
                                                }))                                            

    project_logic = forms.CharField(label='作品设计、发明的目的和基本思路、创新点、技术关键和主要技术目标：', 
                        widget=forms.TextInput(attrs={'placeholder': '2000字内', 
                                                'class': 'form-control',
                                                }))

    technique_point = forms.CharField(label='作品的科学性、先进性', 
                        widget=forms.TextInput(attrs={'placeholder': '500字内', 
                                                'class': 'form-control',
                                                }))

    project_past = forms.CharField(label='作品在何时何地何种机构举行的评审、鉴定、评比、展示等活动中获奖及鉴定结果', 
                        widget=forms.TextInput(attrs={'placeholder': '500字内', 
                                                'class': 'form-control',
                                                }))

    project_stage = forms.CharField(label='作品所处阶段', 
                        widget=forms.TextInput(attrs={'placeholder': '100字内', 
                                                'class': 'form-control',
                                                }))                                            

    technique_transport_method = forms.CharField(label='技术转让方式', 
                        widget=forms.TextInput(attrs={'placeholder': '', 
                                                'class': 'form-control',
                                                }))

    project_show_way = forms.CharField(label='作品可展示形式', 
                        widget=forms.TextInput(attrs={'placeholder': '', 
                                                'class': 'form-control',
                                                }))

    project_predict = forms.CharField(label='使用说明及该作品的技术特点和优势，提供该作品的适用范围及推广前景的技术性说明及市场分析和经济效益预测', 
                        widget=forms.TextInput(attrs={'placeholder': '1000字内', 
                                                'class': 'form-control',
                                                }))
    project_patent = forms.CharField(label='专利申报情况', 
                        widget=forms.TextInput(attrs={'placeholder': '', 
                                                'class': 'form-control',
                                                }))
    project_problem_statement = forms.CharField(label='当前国内外同类型课题研究水平概述', 
                        widget=forms.TextInput(attrs={'placeholder': '1000字内', 
                                                'class': 'form-control',
                                                }))

    #上传

    upload_paper = forms.CharField(label='上传论文文档', 
                        widget=forms.TextInput(attrs={'placeholder': '', 
                                                'class': 'form-control',
                                                }))
    upload_affix = forms.CharField(label='上传附件材料', 
                        widget=forms.TextInput(attrs={'placeholder': '', 
                                                'class': 'form-control',
                                                }))

    upload_picture = forms.CharField(label='上传图片', 
                        widget=forms.TextInput(attrs={'placeholder': '', 
                                                'class': 'form-control',
                                                }))
    upload_video = forms.CharField(label='上传视频', 
                        widget=forms.TextInput(attrs={'placeholder': '', 
                                                'class': 'form-control',
                                                }))
    postscript = forms.CharField(label='备注', 
                        widget=forms.TextInput(attrs={'placeholder': '100字内', 
                                                'class': 'form-control',
                                                }))
    






    class Meta:
        model = Tiaozhancup
        exclude = (
            'student',
            'is_review_by_school',
            'is_review_by_college',
            'is_review_by_boss',
            'school_staff_give',
            'college_staff_give',
            'boss_staff_give',
            'is_pass',
            'is_fail',
            'is_reviewing',
        )
        # fields = '__all__'
        # fields = [
        #     # 'apply_department',
        #     # 'apply_time',
        #     # 'contact_info',
        #     # 'applyer',
        #     # 'apply_place',
        #     # 'what_u_need_to_do',
        #     # 'equipment_u_want',
        # ]

class Tiaozhancup_for_review(forms.Form):
    YES_NO = ((True, '是'), (False, '否'))
    decision = forms.BooleanField(label='是否审核通过',required=False,
                                        widget=forms.RadioSelect(
                                        choices=YES_NO, 
                                        attrs={'class': 'form-control', 
                                                'required':True,
                            }))
    comment = forms.CharField(label='留言', 
                    widget=forms.TextInput(
                                    attrs={'class': 'form-control',
                                    'placeholder': '简短说明',
                                }))
                                