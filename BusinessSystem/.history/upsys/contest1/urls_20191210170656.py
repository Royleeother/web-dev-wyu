from django.contrib import admin
from django.urls import path, include
from contest1 import views
from .views import (
        FormCreateView
    )
from contest1.views import InfoUpdateView
app_name = "contest1"

urlpatterns = [
    path('', views.contest1, name='contest1'),
    path('create/', FormCreateView.as_view(), name='create_form'),
    path('review/', views.reviewpage, name='contest1_review'),
    path('form/<str:sid>/', views.showform, name='contest1_showform'),
    path('update/<int:pk>/', InfoUpdateView.as_view(), name='contest1_update'),
]
