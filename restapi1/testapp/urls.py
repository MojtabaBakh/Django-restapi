
from django.contrib import admin
from django.urls import path , include
from .views import student_list , student_save

urlpatterns = [
 
    path('student_list', student_list),
    path('student_save', student_save),

]
