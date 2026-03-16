from django.db import models

# Create your models here.
class teacher(models.Model):
    Name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)

class assessment(models.Model):
    Name = models.CharField(max_length=25)
    Unit = models.CharField(max_length=30)
    StartDate = models.DateField()
    DueDate = models.DateField()

class Course(models.Model):
    Name = models.CharField(max_length=25)
    Unit = models.CharField(max_length=30)

class Student(models.Model):
    Name = models.CharField(max_length=25)
    Unit = models.CharField(max_length=30)

class Unit(models.Model):
    Name = models.CharField(max_length=25)
    Unit = models.CharField(max_length=30)
