from django.db import models

# Create your models here.
#models are tables i guess

class Todo(models.Model):
    content = models.TextField()  #setting type of table

class test_status_managed(models.Model):
    test_run_id = models.IntegerField()
    test_case = models.TextField()
    on_meter = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.TextField()
