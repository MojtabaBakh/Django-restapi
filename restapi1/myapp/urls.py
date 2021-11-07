
from django.contrib import admin
from django.urls import path

from .views import student_list , student_details , student_save , student_update , student_delete

urlpatterns = [
    path('student_list/', student_list),
    path('student_details/<pk>', student_details),
    path('student_save', student_save),
    path('student_update/<pk>', student_update),
    path('student_delete/<pk>', student_delete),
]
