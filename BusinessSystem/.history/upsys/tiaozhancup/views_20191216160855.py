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
