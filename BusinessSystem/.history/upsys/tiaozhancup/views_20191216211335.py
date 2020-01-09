from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Tiaozhancup
from .forms import TiaozhancupForm

# 开封菜
def tiaozhancup(request):
    user = request.user

    if user.is_student and user.student != None:
        pass
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
                print("temp:", temp)
                temp.append(self.contest_name)
                user.contest = str(temp)
        return super(FormCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(FormCreateView, self).get_context_data(**kwargs)
        return context
