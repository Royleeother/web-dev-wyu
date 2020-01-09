from django.contrib import admin
from django.urls import path, include
from userprofile import views

app_name = "userprofile"

urlpatterns = [
    path('', views.infopage, name='userprofile'),
]
