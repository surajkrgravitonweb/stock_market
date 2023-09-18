from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path , include
from .views import LoginViewSet

router=DefaultRouter()
router.register('account_login',LoginViewSet)

urlpatterns = [
    path('',include(router.urls))
]