from django.db import models

# Create your models here.

class MainContact(models.Model):

    id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)

   

 

    def __str__(self):

        return self.firstname or ' '