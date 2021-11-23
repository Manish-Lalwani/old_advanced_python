from django.db import models


#creating a table(each class represents a table here)
class Company(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name #will return name instead of <****object****>


class Language(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

#creating table programmer and using  Company table name column as foreign key
class Programmer(models.Model):
    name=models.CharField(max_length=20)
    company_name = models.ForeignKey(Company,on_delete=models.CASCADE) #cascade means ut will remove the ref of company which does not exist
    languages = models.ManyToManyField(Language)
    def __str__(self):
        return self.name #will return name instead of <****object****>

