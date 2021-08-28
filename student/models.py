from django.db import models

# Create your models here.
class Student(models.Model):
    firstname =   models.CharField(max_length=100)
    lastname =    models.CharField(max_length=100)
    enrol =       models.CharField(max_length=100)
    semester =    models.IntegerField()
    branch   =    models.CharField(max_length=100)
    course   =    models.CharField(max_length=50)
    email    =    models.EmailField(unique=True)
    mobile_no =   models.CharField(max_length=12)
    address  =    models.TextField(max_length=200)
    fees    =     models.IntegerField(default=0)
    status  =     models.IntegerField(default=0)
    image  =      models.ImageField(upload_to='pics')