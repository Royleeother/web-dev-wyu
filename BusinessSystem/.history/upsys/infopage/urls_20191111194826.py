from django.contrib import admin
from django.urls import path, include
from dashboard import views

app_name = "infopage"

urlpatterns = [
    path('', views.dashboard, name='infopage'),
]
