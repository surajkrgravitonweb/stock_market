import uuid

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone

from .manager import CustomUserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

    # These fields tie to the roles!
    ADMIN = 1
    STAFF = 2
    USER = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (STAFF, 'Staff'),
        (USER, 'User')
    )
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    # Roles created here
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(unique=True)
    
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)


    phone_number=models.CharField(max_length=200,blank=False)
    pancard =models.CharField(max_length=200 ,blank=False )
    bankaccount=models.CharField(max_length=200,blank=False )
    ifsccode=models.CharField(max_length=200,blank=False )
    aadhaarCardNumber=models.CharField(max_length=200 ,blank=False )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    


class OTPVerifiaction(models.Model):
        phone_number = models.IntegerField()
        otp = models.CharField(max_length=4)
        is_verfied = models.BooleanField(default=False)