from django.shortcuts import render
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
        post = request.POST.copy()
        ID = post.get('ID')
        student = Student.objects.get(SID=ID)
        email = student.email
        # SIDs = ''
        # TIDs = ''
        # if ID in SIDs:
        #     pass
        # elif ID in TIDs:
        #     pass
        # else:
        #     return
        post['email'] = email
        request.POST = post
        data = request.POST
        print("data:", data)
        print("email：", email)
        return super(auth_views.PasswordResetView, self).post(request, *args, **kwargs)
    
    # def form_valid(self, form):
    #     # haha = form.save(commit=False)
    #     # data = self.request
    #     # print("data", data)
    #     # print("haha", haha)
    #     print("form", form)
    #     return super(auth_views.PasswordResetView, self).form_valid(form)

