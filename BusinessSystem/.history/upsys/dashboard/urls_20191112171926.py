from django.contrib import admin
from django.urls import path, include
from dashboard import views

app_name = "dashboard"

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('signup/', dashboard.signupView, name='signup'),
    path('signup/student/', dashboard.StudentSignUpView.as_view(), name='student_signup'),
    path('signup/teacher/', dashboard.TeacherSignUpView.as_view(), name='teacher_signup'),
]
