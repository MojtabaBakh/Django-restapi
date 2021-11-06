from django.db import models

# Create your models here.

class Student(models.Model):
    Name=models.CharField(max_length=100)
    Family=models.CharField(max_length=100)
    Code=models.CharField(max_length=100)



