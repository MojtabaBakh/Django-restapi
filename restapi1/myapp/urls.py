
from django.contrib import admin
from django.urls import path

from .views import student_list , student_details , student_save , student_update , student_delete

urlpatterns = [
    path('student-list/', student_list),
    path('student-details/<pk>', student_details),
    path('student-save', student_save),
    path('student-update/<pk>', student_update),
    path('student-delete/<pk>', student_delete),
]
