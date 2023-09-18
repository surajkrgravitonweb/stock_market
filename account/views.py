from django.shortcuts import render
from .models import AccountLogin
from .serializers import LoginSerializers
from rest_framework import viewsets



class LoginViewSet(viewsets.ModelViewSet):
    queryset=AccountLogin.objects.all()
    serializer_class=LoginSerializers
