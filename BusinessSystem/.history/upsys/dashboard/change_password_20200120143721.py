from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from .forms import Password_first_step
from .models import Student, Teacher, User

def forgot_password(request):
    return render(request, 'forget_password.html')

class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = 'reset_password/password_reset.html'
    form_class = Password_first_step
    
    def post(self, request, *args, **kwargs):
        #.data.get('email')
        post = request.POST
        ID = post.get('ID')
        email_post = post.get('email')
        email_by_user = ''
        query_set = Student.objects.filter(SID=ID)
        print("data:", post)
        if len(query_set) == 0:
            return render(request, 'reset_password/password_reset.html', context={"message": '你输入的学号不存在，请确认'})
        email_by_user = query_set.email
        if email_post == email_by_user:
            print("邮件已发送")
            return super(auth_views.PasswordResetView, self).post(request, *args, **kwargs)
        else:
            print("邮件未发送")
            return render(request, 'reset_password/password_reset.html', context={"message": '你输入的邮箱与注册时的邮箱不符合，请重新输入'})
    # def form_valid(self, form):
    #     # haha = form.save(commit=False)
    #     # data = self.request
    #     # print("data", data)
    #     # print("haha", haha)
    #     print("form", form)
    #     return super(auth_views.PasswordResetView, self).form_valid(form)

