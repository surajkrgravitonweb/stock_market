
from django.urls import path
# from .views import UserList
from .views import *


urlpatterns = [
    path("register/", UserList.as_view(), name = "register"),
    path('login/', AuthUserLoginView.as_view(), name = "login"),
    path('checkOTP/', checkOTP ),
    path('sendOTP/',otpGeneration),

]