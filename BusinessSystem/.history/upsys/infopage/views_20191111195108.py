from django.shortcuts import render

# Create your views here.
def infopage(request):
    return render(request, 'dashboard.html')