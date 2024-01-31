from django.db import models

# Create your models here.

class data(models.Model):
    firstname = models.CharField(max_length = 200, null=True)
    lastname = models.CharField(max_length = 200, null=True)
    email = models.CharField(max_length = 200, null=True)
    phone = models.IntegerField()
    password = models.CharField(max_length = 200, null=True)
    gender = models.CharField(max_length=1,blank=True, null=True)