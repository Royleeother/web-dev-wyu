from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Contest1
from dashboard.models import Student, Teacher
from .forms import Contest1Form
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

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
    for k, v in status_dict.items():
        print("current k:", k)
        print("current v:", v)
        if v:
            return status[k]
    return '表单注册、或者审核的时候忘记改状态了！！！程序员出来挨打！！！'

# 这是被授权审核比赛的老师的工号名单
authorize_TID = {
    't1': '厅室管理员',
    't2': '校律委管理员',
    't3': '团委管理员',
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

giveAuthority('Contest1')

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

def reviewpage(request):
    contest_is_reviewing = Contest1.objects.all()
    test = []
    for cc in contest_is_reviewing:
        test.append(Contest1Form(instance=cc))

    content = {
        'contest_is_reviewing':contest_is_reviewing,
        'test':test, 
        'authorize_TID':authorize_TID,
        'authorize_TID_keys':authorize_TID.keys()
    }
    return render(request, 'contest1_review.html', content)
# db.sqlite3

@login_required
def showform(request, id):
    content = {

    }
    return render(request, 'contest1_form_to_grade.html', content)

