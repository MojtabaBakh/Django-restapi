from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer



# Create your views here.


@api_view(["GET"])
def student_list(request):
    students=Student.objects.all()
    students_serializer=StudentSerializer(students , many = True)
    return Response(students_serializer.data)


@api_view(["GET"])
def student_details(request , pk):
    student=Student.objects.get(id=pk)
    student_serializer=StudentSerializer(student , many = False)
    return Response(student_serializer.data)


@api_view(["POST"])
def student_save(request):
    student=StudentSerializer(data=request.data)
    if (student.is_valid()) :
        student.save()

    return Response(student.data)


@api_view(["POST"])
def student_update(request , pk):
    instance=Student.objects.get(id=pk)
    student=StudentSerializer( instance=instance , data=request.data)
    if(student.is_valid()):
        student.save()

    return Response(student.data)   



@api_view(["DELETE"])
def student_delete(request , pk):
    instance=Student.objects.get(id=pk)
    instance.delete()

    return Response("student deleted")    




