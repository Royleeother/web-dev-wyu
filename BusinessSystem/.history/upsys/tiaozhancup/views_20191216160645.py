from django.shortcuts import render

# Create your views here.

# 开封菜
def tiaozhancup(request):
    content = {

    }
    return render(request, 'tiaozhancup.html', content)
