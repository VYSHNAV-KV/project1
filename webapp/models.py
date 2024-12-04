from django.db import models

class contactdb(models.Model):
    Name= models.CharField(max_length=100,blank=True,null=True)
    Mobile = models.IntegerField(blank=True, null=True)
    Email = models.EmailField(max_length=100, blank=True, null=True)
    Message = models.CharField(max_length=100, blank=True, null=True)

class signupdb(models.Model):
    Name = models.CharField(max_length=100, blank=True, null=True)
    Mobile = models.IntegerField(blank=True, null=True)
    Email = models.EmailField(max_length=100, blank=True, null=True)
    Password = models.CharField(max_length=100, blank=True, null=True)
    Re_password = models.CharField(max_length=100, blank=True, null=True)

# Create your models here.
class cartdb(models.Model):
    Username = models.CharField(max_length=100, blank=True, null=True)
    Productname = models.CharField(max_length=100, blank=True, null=True)
    Quantity = models.IntegerField(blank=True, null=True)
    Price = models.IntegerField(blank=True, null=True)
    Totalprice = models.IntegerField(blank=True, null=True)
class orderdb(models.Model):
    Name= models.CharField(max_length=100, blank=True, null=True)
    Email= models.EmailField(max_length=100, blank=True, null=True)
    Place= models.CharField(max_length=100, blank=True, null=True)
    Address= models.CharField(max_length=100, blank=True, null=True)
    Mobile= models.IntegerField(blank=True, null=True)
    Message= models.CharField(max_length=100, blank=True, null=True)
    Totalprice= models.IntegerField(blank=True, null=True)