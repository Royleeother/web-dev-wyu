from django.contrib import admin
from django.urls import path, include
from contest1 import views

app_name = "contest1"

urlpatterns = [
    path('', views.contest1, name='contest1'),
    path('create/', SubjectCreateView.as_view(), name='create_subject'),

]
