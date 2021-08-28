from django.db import models

# Create your models here.
class Faculty(models.Model):
    firstname =   models.CharField(max_length=100)
    lastname =    models.CharField(max_length=100)
    enroll =      models.CharField(max_length=100)
    branch   =    models.CharField(max_length=100)
    course   =    models.CharField(max_length=50)
    email    =    models.EmailField(unique=True)
    mobile_no =   models.CharField(max_length=12)
    address  =    models.TextField(max_length=200)
    image  =      models.ImageField(upload_to='pics')