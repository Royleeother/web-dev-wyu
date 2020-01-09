from django.shortcuts import render

def forgot_password(request):
    return render(request, 'forget_password.html')