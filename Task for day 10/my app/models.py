from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    fees = models.IntegerField()
    gender = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    salary = models.IntegerField()
    gender = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name