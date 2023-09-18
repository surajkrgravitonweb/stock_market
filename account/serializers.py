from rest_framework import serializers
from .models import AccountLogin

class LoginSerializers(serializers.ModelSerializer):
    class Meta:
        model=AccountLogin
        fields='__all__'