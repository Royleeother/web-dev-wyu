from django.contrib import admin
from django.urls import path, include
from dashboard import views

app_name = "userprofile"

urlpatterns = [
    path('', views.index, name='home'),
]
