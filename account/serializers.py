from rest_framework import serializers
from .models import *

class LoginSerializers(serializers.ModelSerializer):
    class Meta:
        model=AccountLogin
        fields='__all__'
class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model=AccountReigster
        fields='__all__'