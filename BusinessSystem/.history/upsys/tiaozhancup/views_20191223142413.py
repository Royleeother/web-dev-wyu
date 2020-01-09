from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Tiaozhancup
from dashboard.models import Student
from .forms import TiaozhancupForm, Tiaozhancup_for_review
from .pool import *
from upsys.tools import school_name_trans, getStatus, they_are_teacher
from tiaozhancup.judge_list import judge_list

## 初始化
# they_are_teacher(['ls1',
#                 'ls2',
#                 'ls3',
#                 'zb1',
#                 'zb2',
#                 'zb3',
# ])
## 

# 开封菜
def tiaozhancup(request):
    user = request.user
    status = '()'
    student_contest_id = '()'

    if user.is_student and user.student != None:
        user = request.user.student
        contest_by_user = Tiaozhancup.objects.filter(student=user)
        if len(contest_by_user) != 0 :
            print("query set:", contest_by_user[0])
            status = getStatus(contest_by_user[0])
            print('status:', status)
            student_contest_id = contest_by_user[0].id
            
        # test
        
        # test
        contest_list = user.contest
        if contest_list != None:
            contest = eval(contest_list)
            print("是个列表", contest_list)
        else:
            contest = []
    else:
        pass
        contest_list = ''
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
        contest.student = self.request.user.student
        contest.save()
        is_teacher = self.request.user.is_teacher
        is_student = self.request.user.is_student
        print("is_teacher: ", is_teacher)
        print("is_student: ", is_student)
        if is_student:
            user = self.request.user.student
            if user.contest == None:
                user.contest = '["{}"]'.format(self.contest_name)
            else:
                temp = eval(user.contest)
                print("temp before:", temp)
                temp.append(self.contest_name)
                print("temp after:", temp)
                user.contest = str(temp)
            user.save()
            ######
            ###
            # 这里是把他扔进院池
            print("康康contest有什么：", contest)
            school = user.school
            print("康康user有什么：", school)
            school_pool = School_pool.objects.all()[0]
            print("康康school_pool有什么：", school_pool)
            # 进入
            what_school = school_name_trans[school]
            temp = eval(getattr(school_pool, what_school))
            print("temp:", temp)
            temp.append(str(user.user.id))
            setattr(school_pool, what_school, str(temp)) 
            school_pool.save()
            print("康康pool有什么：", getattr(school_pool, what_school))
            ###
            ######
        return super(FormCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(FormCreateView, self).get_context_data(**kwargs)
        return context

def reviewpage(request):
    user = request.user.teacher
    teacher_is_authorized = False
    sid_list = ''
    judge_type = ''

    school_pool = School_pool.objects.all()[0]
    college_pool = College_pool.objects.all()[0]
    boss_pool = Boss_pool.objects.all()[0]


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
            sid_list = eval(stage + "_pool")
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

def showform(request, sid, judge_type):
    give_grade_form = Tiaozhancup_for_review()
    student = Student.objects.get(SID = sid)
    student_contest = Tiaozhancup.objects.get(student=student)
    student_form = TiaozhancupForm(instance=student_contest)

    content = {
        'give_grade_form': give_grade_form,
        'student_form': student_form
    }

    print("student_contest: ", student_contest)

    if request.method == 'POST':
        user = request.user.teacher
        form = Tiaozhancup_for_review(data=request.POST)        
        if form.is_valid():
            print("valid valid valid\r\n")
            form_cd = form.cleaned_data
            print("form_cd:", form_cd)
            
            staff_give = judge_type + "_staff_give"
            give_dict = eval(getattr(student_contest, staff_give))
            give_dict[user.TID] = '[{}, {}]'.format(form_cd['decision'], form_cd['comment'])
            print('give_dict', give_dict)
            form_value = str(give_dict)
            setattr(student_contest, staff_give, form_value)
            student_contest.save()
            print("save la")
            # 防止重复提交功能
            #
            give_dict = eval(getattr(student_contest, staff_give))
            department = user.department
            check_if_move_pool(give_dict, department)

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


def check_if_move_pool(give_dict, department):
    print("pool:", give_dict)
    print("department", department)
    return