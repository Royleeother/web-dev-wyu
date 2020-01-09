from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Tiaozhancup
from .forms import TiaozhancupForm
from .pool import *
from upsys.tools import school_name_trans

# 开封菜
def tiaozhancup(request):
    user = request.user

    if user.is_student and user.student != None:
        
        # test
        user = request.user.student.user
        print("康康id是什么鸟：", user.id)
        print("康康student_id是什么鸟：", user.pk)
        # test
    else:
        pass
    content = {

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
            temp.append(str(user.username))
            setattr(school_pool, what_school, str(temp)) 
            school_pool.save()
            print("康康pool有什么：", getattr(school_pool, what_school))
            ###
            ######
        return super(FormCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(FormCreateView, self).get_context_data(**kwargs)
        return context
