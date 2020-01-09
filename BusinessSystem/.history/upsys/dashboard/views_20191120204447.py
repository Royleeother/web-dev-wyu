from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from .forms import StudentSignUpForm, TeacherSignUpForm
from .models import User
# 要引入比赛的一些东西，迟点写个函数把它包起来
from contest1.views import getStatus
from contest1.models import Contest1

# 开封菜
def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print("\nUser Name = ",username)
        print("Password = ",password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('infopage:infopage')
        else:
            context = {'message':'无效 无效 无效 无效 ！！！'}
            return render(request, 'index.html', context)
    username = request.user
    context = {'name': 'hahahah', 'pass': 'jj$L', 'username':username}
    print("ming ming :", username)
    # 'username':username
    return render(request, 'index.html', context)

def contest_status_dict(user, contest_list):
    contest_dict = {}
    for c_name in contest_list:
        command = c_name + '.objects.filter(student=user)[0]'
        print('command: ', command)
        cc = eval(command)
        status = getStatus(cc)
        print("dashboard status:", status)
        contest_dict[c_name] = status
        print("contest_dict:", contest_dict)

def dashboard(request):
    student_contest = ''
    teacher_authorize = ''
    student_contest_status = {}

    if request.user.is_student:
        user = request.user.student
        student_contest = eval(user.contest)
        student_contest_status = contest_status_dict(user, student_contest)

    else:
        user = request.user.teacher
        teacher_authorize = eval(user.authorization_for_contest)
    content = {
        'student_contest': student_contest,
        'teacher_authorize': teacher_authorize,
        'student_contest_status': student_contest_status,
    }
    return render(request, 'dashboard.html', content)

def signupView(request):
    return render(request, 'signup.html')

class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('infopage:infopage')

class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('infopage:infopage')

def user_logout(request):
    logout(request)
    return redirect("home")