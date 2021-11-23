from django.db import models

# Create your models here.

class Employee(models.Model):
    ename = models.CharField(max_length=255)
    edesg = models.CharField(max_length=30)





