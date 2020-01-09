from django.contrib import admin
from django.urls import path, include
from dashboard import views

app_name = "dashboard"

urlpatterns = [
    path('', views.index, name='home'),
    path('', views.dashboard, name='dashboard')
]
