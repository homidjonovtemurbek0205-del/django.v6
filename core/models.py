from django.db import models

class Student(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField()
    email = models.EmailField()
    bio = models.TextField()