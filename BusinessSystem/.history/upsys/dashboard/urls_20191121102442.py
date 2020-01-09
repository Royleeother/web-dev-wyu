from django.contrib import admin
from django.urls import path, include
from dashboard import views

app_name = "dashboard"

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('signup/', views.signupView, name='signup'),
    path('signup/student/', views.StudentSignUpView.as_view(), name='student_signup'),
    path('signup/teacher/', views.TeacherSignUpView.as_view(), name='teacher_signup'),
    path('logout/', views.user_logout, name='logout'),
    path('update_student_info', views.StudentInfoUpdateView.as_view(), name='S_update'),
]
