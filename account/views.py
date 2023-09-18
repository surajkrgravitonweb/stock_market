from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.views import APIView
from django.http import HttpResponse

class LoginViewSet(viewsets.ModelViewSet):
    queryset=AccountLogin.objects.all()
    serializer_class=LoginSerializers
class RegisterViewSet(viewsets.ModelViewSet):
    queryset=AccountReigster.objects.all()
    serializer_class=RegisterSerializers
from django.core import serializers
class UserLoginView(APIView):
    def post(self, request, format=None):
        username=request.data.get("username")
        password=request.data.get("password")
        s=AccountReigster.objects.filter(username=username,password=password)
        s1 = serializers.serialize('json', s)
        print(username,password,s)
        return HttpResponse(s1, content_type='application/json')

