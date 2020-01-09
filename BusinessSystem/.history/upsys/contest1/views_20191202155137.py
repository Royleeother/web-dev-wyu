from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Contest1
from dashboard.models import Student, Teacher
from .forms import Contest1Form, Contest1_for_review
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils import timezone


# Create your views here.
def getStatus(contest):
    status_dict = dict(
        is_pass = contest.is_pass,
        is_reviewing = contest.is_reviewing,
        is_fail = contest.is_fail,
    )
    status = dict(
        is_pass = '已通过',
        is_reviewing = '正在审核',
        is_fail = '审核不通过',
    )
    # for k, v in status_dict.items():
    #     print("current k:", k)
    #     print("current v:", v)
    #     if not v:
    #         return status[k]
    # 先来个土法炼钢，赶时间
    if status_dict['is_reviewing']:
        return status['is_reviewing']
    elif status_dict['is_pass']:
        return status['is_pass']
    else:
        return status['is_fail']

    # return '表单注册、或者审核的时候忘记改状态了！！！程序员出来挨打！！！'

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

# giveAuthority('Contest1')

def contest1(request):
    user = request.user
    status = '()'
    test = '()'
    # cc = Contest1.objects.get(pk=1)
    # teacher_all = Teacher.objects.all()
    # student_aa = Student.objects.filter(ddd=user)
    # teacher_aa = Teacher.objects.filter(TID=user.teacher.TID)[0].TID
    
    if user.is_student and user.student != None:
        user = request.user.student
        contest_by_user = Contest1.objects.filter(student=user)
        # contest_by_user = Contest1.objects.get(student=user)
        print("contest_by_user", len(contest_by_user))
        # status
        if len(contest_by_user) != 0 :
            print("query set:", contest_by_user[0])
            status = getStatus(contest_by_user[0])
            print('status:', status)
            
        contest = user.contest
        if contest != None:
            contest = eval(contest)
            print("是个列表", contest)
        else:
            contest = []
        student_contest_id = contest_by_user[0].id
    else:
        contest = []
        user = request.user.teacher
        contest_is_reviewing = Contest1.objects.all()
        if len(contest_is_reviewing) != 0:
            test = Contest1Form(instance=contest_is_reviewing[0])
        print(test)

    content = {
        'contest_list': contest,
        'status': status,
        # 'teacher_all': teacher_all,
        # 'teacher_aa': teacher_aa,
        # 'student_aa': student_aa,
        'test': test,
        'student_contest_id': student_contest_id,
    }
    # print("contest_list:", content['contest_list'])
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
            if user.contest == None:
                user.contest = '["{}"]'.format(self.contest_name)
            else:
                temp = eval(user.contest)
                print("temp:", temp)
                temp.append(self.contest_name)
                user.contest = str(temp)
        user.save()
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
        request_user = self.request.user
        request = self.request.SID
        # contest_user = Contest1(form)
        # print("康康form:", form)
        print("request:", request)
        print("用户***:", request_user)
        # print("ddddddd", contest_user)
        contest = form.save(commit=False)
        contest.updated_by = request_user
        contest.updated_at = timezone.now()
        contest.save()
        
        return redirect("contest1:contest1")
        # return super().form_valid(form)

def reviewpage(request):
    contest_is_reviewing = Contest1.objects.all()
    gg = contest_is_reviewing[1]
    
    # for cc in contest_is_reviewing:
    #     test.append(Contest1Form(instance=cc))

    content = {
        'contest_is_reviewing':contest_is_reviewing,
        'authorize_TID':authorize_TID,
        'authorize_TID_keys':authorize_TID.keys()
    }

        
    return render(request, 'contest1_review.html', content)
# db.sqlite3

@login_required
def showform(request, sid):
    contest_is_reviewing = Contest1.objects.all()
    student = Student.objects.get(SID = sid)
    student_contest = Contest1.objects.get(student=student)
    name = request.user.username
    give_grade = Contest1_for_review(review_type=staff[name])

    content = {
        'student_id': sid,
        'authorize_TID_keys': authorize_TID.keys(),
        'student_contest': student_contest,
        'student_form': Contest1Form(instance=student_contest),
        'give_grade': give_grade,
    }
    print("现在的用户是谁：", request.user.username)
    print("传入的id：", sid)
    print("student_contest: ", student_contest)
    # print("give_grade:", give_grade)

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
            change_contest_status(student_contest)
            return redirect("contest1:contest1_review")
        else:
            print('invalid form???')
            print("form:", form)

    return render(request, 'contest1_form_to_grade.html', content)

def change_contest_status(student_contest):
    decisions = {}
    Not_pass_by_whom = []
    for item in decision.items():
        dd = getattr(student_contest, item[1])
        people = item[0]
        decisions[people] = dd
    print("decisions lalaal:", decisions)
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

# def change_status_simple()