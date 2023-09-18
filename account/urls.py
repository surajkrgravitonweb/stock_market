from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path , include
from .views import *

router=DefaultRouter()
router.register('account_login',LoginViewSet,basename='loginview')
router.register('account_register',RegisterViewSet,basename='registerView')

urlpatterns = [
    path('',include(router.urls)),
    path('login/', UserLoginView.as_view(), name='login'),
  
]