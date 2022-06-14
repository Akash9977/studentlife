from turtle import title
from django.db import models

# Create your models here.

class Department(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title
        
class Gender(models.Model):
    gname=models.CharField(max_length=30)

    def __str__(self):
        return self.gname

class Student(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.EmailField(max_length=30)
    Cell=models.CharField(max_length=20)
    Department=models.ForeignKey(Department, on_delete=models.CASCADE)
    Gender=models.ForeignKey(Gender, on_delete=models.CASCADE)
    YourMessage=models.CharField(max_length=500)
    Picture=models.ImageField(null=True, blank=True)