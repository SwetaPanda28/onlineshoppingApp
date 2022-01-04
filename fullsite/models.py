from django.db import models
from authentication.models import User 
from phonenumber_field.modelfields import  PhoneNumberField
# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=20)
    product_desc=models.CharField(max_length=100)
    pub_date=models.DateField()
    price=models.FloatField(max_length=99999999)
    product_img=models.ImageField(upload_to='items/')

class Cart(models.Model):
   user=models.OneToOneField(User,on_delete=models.CASCADE)
   products=models.ManyToManyField(Product)
   

class Address(models.Model):
    name=models.CharField(max_length=20)
    phonenum=PhoneNumberField()
    alternative_phno=PhoneNumberField(blank=True)
    pincode=models.IntegerField()
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    houseadd=models.CharField(max_length=200)
    area=models.CharField(max_length=100)
    user=models.ManyToManyField(User)