from django.shortcuts import render
from django.contrib.auth import views as auth_views

def forgot_password(request):
    return render(request, 'forget_password.html')

class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = 'reset_password/password_reset.html'