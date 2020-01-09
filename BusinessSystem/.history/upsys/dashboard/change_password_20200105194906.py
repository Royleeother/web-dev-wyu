from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django import forms

def forgot_password(request):
    return render(request, 'forget_password.html')

class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = 'reset_password/password_reset.html'
    form_class = 
    
    def post(self, request, *args, **kwargs):
        #.data.get('email')
        post = request.POST.copy()
        email = request.POST.get('email')
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

class password_first_step(forms.Form):
    ID = forms.CharField(label='学号', 
                    widget=forms.TextInput(attrs={'placeholder': '', 
                                            'class': 'form-control',
                                            }))