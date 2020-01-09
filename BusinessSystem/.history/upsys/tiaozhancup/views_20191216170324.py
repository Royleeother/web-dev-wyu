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
        pass

    def get_context_data(self, **kwargs):
        pass
