from django.shortcuts import render

# Create your views here.

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
    model = Contest1
    form_class = Contest1Form
    # 奇技淫巧
    contest_name = 'Contest1'