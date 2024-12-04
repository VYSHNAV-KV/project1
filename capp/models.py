from django.db import models


class categorydb(models.Model):
    Categoryname=models.CharField(max_length=100,null=True,blank=True)
    Description=models.CharField(max_length=100,null=True,blank=True)
    Categoryimage=models.ImageField(upload_to="category_image",null=True,blank=True)
# Create your models here.

class productdb(models.Model):
    Categoryname = models.CharField(max_length=100, null=True, blank=True)
    Productname = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Mrp= models.IntegerField(null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Country = models.CharField(max_length=100, null=True, blank=True)
    Manufactured = models.CharField(max_length=100, null=True, blank=True)
    Productimage1 = models.ImageField(upload_to="product_image", null=True, blank=True)
    Productimage2 = models.ImageField(upload_to="product_image", null=True, blank=True)
    Productimage3 = models.ImageField(upload_to="product_image", null=True, blank=True)

