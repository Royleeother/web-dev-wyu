from django.shortcuts import render
from django.contrib.auth import views as auth_views

def forgot_password(request):
    return render(request, 'forget_password.html')

class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = 'reset_password/password_reset.html'
    
    def post(self, request, *args, **kwargs):
        #.data.get('email')
        email = request.POST.get('email')
        print("email：", email)
        return super(auth_views.PasswordResetView, self).post(request, *args, **kwargs)
    
    # def form_valid(self, form):
    #     # haha = form.save(commit=False)
    #     # data = self.request
    #     # print("data", data)
    #     # print("haha", haha)
    #     print("form", form)
    #     return super(auth_views.PasswordResetView, self).form_valid(form)