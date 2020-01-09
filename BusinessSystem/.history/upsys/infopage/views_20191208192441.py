from django.shortcuts import render

# Create your views here.
def infopage(request):
    user = request.user

    context = {
        'user': user,
    }
    return render(request, 'infopage.html', context)