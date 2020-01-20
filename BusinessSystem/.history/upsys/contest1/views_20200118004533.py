from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Contest1
from .pool import *
from dashboard.models import Student, Teacher
from .forms import Contest1Form, Contest1_for_review
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse
from upsys.tools import (getStatus, 
                        push_into_contest, 
                        current_time,
)
from contest1.judge_list import judge_list
# Create your views here.

# 这是被授权审核比赛的老师的工号名单
authorize_TID = {
    't1': '厅室管理员',
    't2': '校律委管理员',
    't3': '团委管理员',
}
staff = {
        '厅室管理员': 'guiding_unit',
        '校律委管理员': 'discipline_unit',
        '团委管理员': 'ccyl'
    }
comment = {
    '厅室管理员': 'guiding_unit_comment',
    '校律委管理员': 'discipline_unit_comment',
    '团委管理员': 'ccyl_comment'
}
decision = {
    '厅室管理员': 'guiding_unit_decision',
    '校律委管理员': 'discipline_unit_decision',
    '团委管理员': 'ccyl_decision'
}

# giveAuthority('Contest1')

# 开封菜
def contest1(request):
    user = request.user
    status = '()'
    student_contest_id = '()'
    
    if user.is_student and user.student != None:
        user = request.user.student
        # 获取用户参加了的这个比赛的信息的那个对象
        contest_by_user = Contest1.objects.filter(student=user)
        print("contest_by_user", len(contest_by_user))
        # status
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
    return render(request, 'contest1.html', content)

class FormCreateView(LoginRequiredMixin, CreateView):
    model = Contest1
    form_class = Contest1Form
    # 奇技淫巧
    contest_name = 'Contest1'
    
    def form_valid(self, form):
        contest = form.save(commit=False)
        print("康康是什么鸟：", self.request.user.student)
        contest.student = self.request.user.student
        contest.upload_time = current_time()
        contest.save()
        is_teacher = self.request.user.is_teacher
        is_student = self.request.user.is_student
        print("is_teacher: ", is_teacher)
        print("is_student: ", is_student)

        if is_teacher:
            user = self.request.user.teacher
            # 申报之类的
        else:
            user = self.request.user.student
            # 改变表单状态，改为正在审核状态
            # Contest1.objects.get(student=user).is_reviewing = True
            # 注入比赛名
            push_into_contest(user, self.contest_name)
            
        return super(FormCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(FormCreateView, self).get_context_data(**kwargs)
        # context['main_page_title'] = 'Subject Creation'
        # context['panel_name'] = 'Subjects'
        # context['panel_title'] = 'Add Subject'
        context['text'] = '我在测试'
        return context

class InfoUpdateView(LoginRequiredMixin, UpdateView):
    model = Contest1
    template_name_suffix = '_form'
    form_class = Contest1Form
    success_url = reverse_lazy('contest1:contest1')

    # change_status_simple(self.objects.pk)

    def get_object(self, queryset=None):
        obj = Contest1.objects.get(pk=self.kwargs['pk'])
        return obj

    # def get_object(self):
    #     id_ = self.kwargs.get("id")
    #     return get_object_or_404(Contest1, id=id_)

    def form_valid(self, form):
        request_user = self.request.user.student
        contest_by_user_id = Contest1.objects.filter(student=request_user)[0].id
        request_form_id = int(self.request.path.split('/')[3])
        # contest_user = Contest1(form)
        # print("康康form:", form)
        print("request:", type(request_form_id))
        print("request:", request_form_id)
        print("用户***:", contest_by_user_id)
        print("用户***:", type(contest_by_user_id))
        # print("ddddddd", contest_user)
        if contest_by_user_id == request_form_id:
            contest = form.save(commit=False)
            contest.updated_by = request_user
            contest.updated_at = timezone.now()
            contest.save()
        else:
            return HttpResponse("gck gck")
        return redirect("contest1:contest1")
        # return super().form_valid(form)

def reviewpage(request):
    # 此处的 contest_is_reviewing 要改成对应的池的学生信息
    user = request.user.teacher
    contest_is_reviewing = ''
    gg = contest_is_reviewing[1]
    sid_list = ''
    judge_type = ''

    stage1_pool = Stage1_pool.objects.all()[0]
    stage2_pool = Stage2_pool.objects.all()[0]
    stage3_pool = Stage3_pool.objects.all()[0]

    # 由老师是什么部门，决定老师可以审核哪个池的信息
    name = user.username

    # for cc in contest_is_reviewing:
    #     test.append(Contest1Form(instance=cc))

    content = {
        'contest_is_reviewing':contest_is_reviewing,
        'authorize_TID':authorize_TID,
        'authorize_TID_keys':authorize_TID.keys()
    }
    return render(request, 'contest1_review.html', content)

#给老师打分的函数
def sss(request, sid, judge_type):
    student = Student.objects.get(SID = sid)
    student_contest = Contest1.objects.get(student=student)
    name = request.user.username
    # give_form()
    # 判断老师是否有资格，并给予不同的表单
    if user.TID in judge_list['boss']:
        give_grade_form = Contest1_for_review(review_type=staff[name])
        student_form = Contest1Form(instance=student_contest)

    if request.method == 'POST':
        user = request.user.teacher
        form = Contest1_for_review(data=request.POST, review_type=staff[name])
        if form.is_valid():
            form_cd = form.cleaned_data
            # 这里的decision 和 comment 都在上面
            dd = decision[name]
            mm = comment[name]
            setattr(student_contest, dd, profile_cd[dd])
            setattr(student_contest, mm, profile_cd[mm])
            student_contest.save()
            check_if_move_pool(give_dict, judge_type, student_contest, department)
            return redirect('/tiaozhancup/review/')
        else:
            print('invalid form???')
            print("form:", form)            

    return render(request, 'contest1_form_to_grade.html', content)

def showform(request, sid):
    contest_is_reviewing = Contest1.objects.all()
    student = Student.objects.get(SID = sid)
    student_contest = Contest1.objects.get(student=student)
    name = request.user.username
    give_grade_form = Contest1_for_review(review_type=staff[name])
    student_form = Contest1Form(instance=student_contest)

    content = {
        'student_id': sid,
        'authorize_TID_keys': authorize_TID.keys(),
        'student_contest': student_contest,
        'student_form': student_form,
        'give_grade_form': give_grade_form,
    }
    print("现在的用户是谁：", request.user.username)
    print("传入的id：", sid)
    print("student_contest: ", student_contest)
    print("give_grade_form:", give_grade_form)

    if request.method == 'POST':
        print("name: ", name)
        print("staff name: ", staff[name])
        form = Contest1_for_review(data=request.POST, review_type=staff[name])
        if form.is_valid():
            print("valid valid valid\r\n")
            profile_cd = form.cleaned_data
            # cc = Contest1.objects.get(student=student_contest.student)
            dd = decision[name]
            mm = comment[name]
            print("dd", dd, type(dd))
            print("mm", mm, type(mm))
            print("\r\n")
            print("profile_cd[dd]", profile_cd[dd])
            print("profile_cd[mm]", profile_cd[mm])
            setattr(student_contest, dd, profile_cd[dd])
            setattr(student_contest, mm, profile_cd[mm])
            # cc.guiding_unit_decision = profile_cd['guiding_unit_decision']
            # cc.guiding_unit_comment = profile_cd['guiding_unit_comment']
            student_contest.save()
            print("save la")
            # 改变审核状态
            change_contest_status(student_contest)
            return redirect("contest1:contest1_review")
        else:
            print('invalid form???')
            print("form:", form)

    return render(request, 'contest1_form_to_grade.html', content)


# HELPER FUNCTION
def change_contest_status(student_contest):
    decisions = {}
    Not_pass_by_whom = []
    # 注意哦，下面的是 decision 不是 decisions，decision是一个字典，在上面
    for item in decision.items():
        dd = getattr(student_contest, item[1])
        people = item[0]
        decisions[people] = dd
    print("decisions laltime_structl:", decisions)
    if None in decisions.values():
        # 有人还没审
        return Not_pass_by_whom
    else:
        student_contest.is_reviewing = False
        if False in decisions.values():
            student_contest.is_fail = True
            student_contest.is_pass = False
            for ii in decisions.items():
                if not ii[1]:
                    Not_pass_by_whom.append(ii[0])
        else:
            student_contest.is_pass = True
            student_contest.is_fail = False
        student_contest.save()
        print("Not_pass_by_whom:", Not_pass_by_whom)
        return Not_pass_by_whom

def giveAuthority(contest_name):
    for tid in authorize_TID.keys():
        teacher = Teacher.objects.filter(TID=tid)[0]
        not_list = teacher.authorization_for_contest
        is_list = eval(not_list)
        if contest_name not in is_list:
            is_list.append(contest_name)
            teacher.authorization_for_contest = str(is_list)
            teacher.save()

        print("teacher.authorization_for_contes:", teacher.authorization_for_contest)

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
        decision = eval(aa.split('[')[1])
        print("decision", decision)
        print("decision", type(decision))
        if decision:
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

