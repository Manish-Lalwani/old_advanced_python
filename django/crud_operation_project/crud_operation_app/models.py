# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TestDataTable(models.Model):
    test_run_id = models.IntegerField(blank=True, null=True)
    test_case = models.TextField(blank=True, null=True)
    on_meter = models.TextField(blank=True, null=True)
    start_time = models.DateField(blank=True, null=True)
    end_time = models.DateField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    status_priority = models.TextField(blank=True, null=True)
    tid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'test_data_table'


#CRUD Operations
#create /insert / add - POST
#retrieve / fetch - GET
# update / edit - PUT
# delete / remove - DELETE