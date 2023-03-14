from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30),
    email = models.EmailField(null=True),
    age = models.IntegerField()
    gender = models.CharField(max_length=30, blank=False, null=False)

def  __str__(self):
    return self.name