from django.shortcuts import render

# Create your views here.
def infopage(request):
    user = request.user

    announce()
    context = {
        'user': user,
    }
    return render(request, 'infopage.html', context)

def announce():
    return 


# 2020-1-9 18:18:56 测试