from django.db import models

# Create your models here.

class AccountLogin(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    
class AccountReigster(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    firstname =models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email   =models.CharField(max_length=200)
    phone_number=models.CharField(max_length=200)
    pancard =models.CharField(max_length=200)
    bankaccount=models.CharField(max_length=200)
    ifsccode=models.CharField(max_length=200)
    aadhaarCardNumber=models.CharField(max_length=200)
