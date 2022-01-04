from authentication.test import Address
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here

class User(models.Model):
    firstname= models.CharField(max_length=20)
    lastname= models.CharField(max_length=20)
    emailAddress= models.EmailField(unique=True)
    phonenumber= PhoneNumberField()
    password=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
