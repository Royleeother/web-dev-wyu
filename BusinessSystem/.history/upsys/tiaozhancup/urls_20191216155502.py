from django.urls import path, include
from tiaozhancup import views
# from .views import (
#         FormCreateView
#     )

app_name = "tiaozhancup"

urlpatterns = [
    path('', views.tiaozhancup, name='tiaozhancup'),
]