from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list),
    path('tasks/<int:id>/', views.task_detail),
]
