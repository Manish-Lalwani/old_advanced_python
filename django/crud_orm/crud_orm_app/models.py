from django.db import models


#Create your models here.
class Department(models.Model):
    did = models.AutoField(primary_key=True)
    dname = models.TextField()

    def __str__(self):
        return self.dname


class Employee(models.Model):
    eid = models.AutoField(primary_key=True)
    ename = models.TextField()
    edesg = models.CharField(max_length=100)
    department = models.ForeignKey(Department,on_delete=models.CASCADE) #i guess it takes the ref of the primary key django attaches one primary key column internally if not externally specified so this is ref to that and not to the whole class or table to be confirmed #if primary key not specified it add a column name id in the table

    def __str__(self):
         return self.ename

# class DemoDepartment(models.Model):
#     did = models.IntegerField(null=False)
#     dname = models.TextField()
#
#     def __str__(self):
#         return self.dname
#
# class Demo(models.Model):
#     eid = models.IntegerField(null=False)
#     ename = models.TextField()
#     edesg = models.CharField(max_length=100)
#     department = models.ForeignKey(DemoDepartment,on_delete=models.CASCADE)  # i guess it takes the ref of the primary key django attaches one primary key column internally if not externally specified so this is ref to that and not to the whole class or table to be confirmed
#
#
#     def __str__(self):
#         return self.ename
#
#
map()