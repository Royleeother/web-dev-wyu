from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Tiaozhancup
from dashboard.models import Student
from .forms import TiaozhancupForm, Tiaozhancup_for_review, Tiaozhancup_for_review_boss, TiaozhancupForm_forboss
from .pool import *
from upsys.tools import (school_name_trans, 
                        getStatus, 
                        they_are_teacher, 
                        push_into_contest,
                        throw_to_pool,
                        current_time,
                        give_form,
                        )
from tiaozhancup.judge_list import judge_list

## 初始化
# they_are_teacher(['ls1',
#                 'ls2',
#                 'ls3',
#                 'zb1',
#                 'zb2',
#                 'zb3',
#                 'xj1',
#                 'xj2',
#                 'xj3',
#                 'zj1',
# ])
## 

# 开封菜
def tiaozhancup(request):
    user = request.user
    status = '()'
    student_contest_id = '()'

    if user.is_student and user.student != None:
        user = request.user.student
        # 获取用户参加了的这个比赛的信息的那个对象
        contest_by_user = Tiaozhancup.objects.filter(student=user)
        # 说明用户报名了这个比赛
        if len(contest_by_user) != 0 :
            print("query set:", contest_by_user[0])
            # 获取比赛审核状态（简易版）
            status = getStatus(contest_by_user[0])
            print('status:', status)
            student_contest_id = contest_by_user[0].id
        #
        contest = user.contest
        if contest != None:
            contest_list = eval(contest)
            print("是个列表, 已参加的比赛", contest_list)
        else:
            contest_list = []
    else:
        contest_list = []

    content = {
        'contest_list': contest_list,
        'status': status,
        'student_contest_id': student_contest_id,
    }
    return render(request, 'tiaozhancup.html', content)

class FormCreateView(LoginRequiredMixin, CreateView):
    model = Tiaozhancup
    form_class = TiaozhancupForm
    # 奇技淫巧
    contest_name = 'Tiaozhancup'

    def form_valid(self, form):
        contest = form.save(commit=False)
        print("康康是什么鸟：", self.request.user.student)
        # 把学生打入contest，再保存
        contest.student = self.request.user.student
        contest.upload_time = current_time()
        contest.save()
        is_student = self.request.user.is_student
        if is_student:
            user = self.request.user.student
            # 把比赛名字放入user.contest
            push_into_contest(user, self.contest_name)
            # 这里是把他扔进院池
            # 扔进最初级的池子
            pool = School_pool.objects.all()[0]
            throw_to_pool(user, pool)
            
        return super(FormCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        # context['text'] = '我在测试'
        context = super(FormCreateView, self).get_context_data(**kwargs)
        return context

# class InfoUpdateView(LoginRequiredMixin, UpdateView):
    model = Tiaozhancup
    # template_name_suffix = '_form'
    # form_class = Contest1Form
    # success_url = reverse_lazy('contest1:contest1')

    def get_object(self, queryset=None):
        # obj = Contest1.objects.get(pk=self.kwargs['pk'])
        # return obj
        return
    
    def form_valid(self, form):
        return
        # request_user = self.request.user.student
        # contest_by_user_id = Contest1.objects.filter(student=request_user)[0].id
        # request_form_id = int(self.request.path.split('/')[3])
        # # contest_user = Contest1(form)
        # # print("康康form:", form)
        # print("request:", type(request_form_id))
        # print("request:", request_form_id)
        # print("用户***:", contest_by_user_id)
        # print("用户***:", type(contest_by_user_id))
        # # print("ddddddd", contest_user)
        # if contest_by_user_id == request_form_id:
        #     contest = form.save(commit=False)
        #     contest.updated_by = request_user
        #     contest.updated_at = timezone.now()
        #     contest.save()
        # else:
        #     return HttpResponse("gck gck")
        # return redirect("contest1:contest1")

def reviewpage(request):
    user = request.user.teacher
    teacher_is_authorized = False
    sid_list = ''
    judge_type = ''

    school_pool = School_pool.objects.all()[0]
    college_pool = College_pool.objects.all()[0]
    boss_pool = Boss_pool.objects.all()[0]

    # 由老师是什么部门，决定老师可以审核哪个池的信息
    for items in judge_list.items():
        stage = items[0]
        biao = items[1]
        department = user.department
        if type(biao) == dict:
            if department in biao.keys():
                if user.TID in biao[department]:
                    teacher_is_authorized = True
                    judge_type = stage
                    # .是为了到达确切位置
                    # 
                    sid_list = eval(stage + "_pool.{}".format(school_name_trans[department]))
                    sid_list = eval(sid_list)
        elif user.TID in biao:
            teacher_is_authorized = True
            judge_type = stage
            sid_list = eval(stage + "_pool." + stage + "_pool")
            sid_list = eval(sid_list)


    contest_is_reviewing = []
    for sid in sid_list:
        ss = Tiaozhancup.objects.get(student_id=int(sid))
        contest_is_reviewing.append(ss)

    print("contest_is_reviewing", contest_is_reviewing)
    print("teacher_is_authorized", teacher_is_authorized)

    content = {
        'contest_is_reviewing':contest_is_reviewing,
        'teacher_is_authorized': teacher_is_authorized,
        'judge_type': judge_type,
    }

    return render(request, 'tiaozhancup_review.html', content)

#给老师打分的函数
def showform(request, sid, judge_type):
    student = Student.objects.get(SID = sid)
    student_contest = Tiaozhancup.objects.get(student=student)
    user = request.user.teacher
    # 针对不同对象，给不同表单
    # give_form(user, judge_list, 
    # student_form_boss='', student_form_normal, 
    # give_grade_form_boss='', give_grade_form_normal,
    
    # )
    if user.TID in judge_list['boss']:
        print("jin ndabshuab")
        student_form = TiaozhancupForm_forboss(instance=student_contest)
        print("bosssss:", student_form)
        give_grade_form = Tiaozhancup_for_review_boss()
    else:
        student_form = TiaozhancupForm(instance=student_contest)
        give_grade_form = Tiaozhancup_for_review()

    content = {
        'give_grade_form': give_grade_form,
        'student_form': student_form
    }

    print("student_contest: ", student_contest)

    if request.method == 'POST':
        user = request.user.teacher
        is_boss = False
        if user.TID in judge_list['boss']:
            print("变了njknjb")
            form = Tiaozhancup_for_review_boss(data=request.POST)
            is_boss = True
        else:
            form = Tiaozhancup_for_review(data=request.POST)        
        if form.is_valid():

            print("valid valid valid\r\n")
            form_cd = form.cleaned_data
            print("form_cd:", form_cd)
            
            staff_give = judge_type + "_staff_give"
            give_dict = eval(getattr(student_contest, staff_give))
            if is_boss:
                give_dict[user.TID] = '[{}]'.format(form_cd['grade'])
            else:
                give_dict[user.TID] = '[{}, {}]'.format(form_cd['decision'], form_cd['comment'])
            print('give_dict', give_dict)
            form_value = str(give_dict)
            setattr(student_contest, staff_give, form_value)
            student_contest.save()
            print("save la")
            if is_boss:
                return redirect('/tiaozhancup/review/')
            # 防止重复提交功能
            #
            give_dict = eval(getattr(student_contest, staff_give))
            department = user.department
            check_if_move_pool(give_dict, judge_type, student_contest, department)
            return redirect('/tiaozhancup/review/')
        else:
            print('invalid form???')
            print("form:", form)

    return render(request, 'tiaozhancup_form_to_grade.html', content)

def announce(request):
    user = request.user

    if user.is_student and user.student != None:
        pass
        # test
        
        # test
    else:
        pass
    content = {

    }
    return render(request, 'tiaozhancup.html', content)

# HELPER FUNCTION
def check_if_move_pool(give_dict, staff_type, student_contest, department=''):
    print("pool:", give_dict)
    print("department", department)
    print("staff_type", staff_type)

    if staff_type == 'school':
        the_list = judge_list[staff_type][department]
    else:
        the_list = judge_list[staff_type]

    print("the_list", the_list)
    keys = give_dict.keys()
    true_count = 0
    for tid in the_list:
        if tid not in keys:
            print("bai bai")
            return
        aa = give_dict[tid].split(',')[0]
        decision = eval(aa.split('[')[1]) # 这是一个布尔值（理想状态下）
        print("decision", decision)
        print("decision", type(decision))
        if decision:
            # 康康是否要以
            true_count += 1
            if true_count == len(the_list):
                is_review_by_xxx = 'is_review_by_' + staff_type
                setattr(student_contest, is_review_by_xxx, True)
                student_contest.save()
                student = student_contest.student
                move_pool(staff_type, student)  
            else:
                print("true_count", true_count)
                print("不够 继续")
        else:
            # 退回下一个池
            # 暂时先写这种，下一个比赛在合并成一个整合型的move_pool
            move_to_previous_pool(current_pool)

def move_to_previous_pool(current_pool):
    pass

def move_pool(staff_type, student):
    print("move_pool", "move_pool")
    student_id = student.user.id
    print("student.id", student.user.id)
    print("student.username", student.username)
    print("student.school", student.school)
    school_name = school_name_trans[student.school]
    print("school_name_trans", school_name_trans[student.school])
    get_pool = {
        'school': School_pool.objects.all()[0],
        'college': College_pool.objects.all()[0],
        'boss': Boss_pool.objects.all()[0],
    }
    
    if staff_type != 'boss':
        move_pool_helper(staff_type, get_pool, school_name, student_id)

    return 

def move_pool_helper(staff_type, get_pool, school_name, student_id):
    print("move_pool_helper")
        # orign_pool = School_pool.objects.all()[0]
    #
    orign_pool = get_pool[staff_type]
    orign_pool_name = staff_type + '_pool'
    #
    if staff_type == 'college':
        next_pool_name = 'boss'
        school_name = orign_pool_name
    elif staff_type == 'school':
        next_pool_name = 'college'
    ## 移除
    the_list = eval(getattr(orign_pool, school_name))
    the_list.remove(str(student_id))
    setattr(orign_pool, school_name, str(the_list))
    orign_pool.save()
    # 写入
    next_pool = get_pool[next_pool_name]
    next_pool_name = next_pool_name + '_pool'
    the_list = eval(getattr(next_pool, next_pool_name))
    the_list.append(str(student_id))
    setattr(next_pool, next_pool_name, str(the_list))
    next_pool.save()
    return 