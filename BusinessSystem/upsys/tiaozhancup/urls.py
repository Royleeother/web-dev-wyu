from django.urls import path, include
from tiaozhancup import views
from .views import (
        FormCreateView
    )

app_name = "tiaozhancup"

urlpatterns = [
    path('', views.tiaozhancup, name='tiaozhancup'),
    path('create/', FormCreateView.as_view(), name='create_form'),
    path('review/', views.reviewpage, name='tiaozhancup_review'),
    path('form/<str:sid>/<str:judge_type>/', views.showform, name='contest1_showform'),
]