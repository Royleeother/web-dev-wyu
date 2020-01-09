from django.contrib import admin
from django.urls import path, include
from contest1 import views
from .views import (
        FormCreateView    
    )

app_name = "contest1"

urlpatterns = [
    path('', views.contest1, name='contest1'),
    path('create/', FormCreateView.as_view(), name='create_subject'),

]
