from django.contrib import admin
from django.urls import path, include
from infopage import views

app_name = "infopage"

urlpatterns = [
    path('', views.infopage, name='infopage'),
]
