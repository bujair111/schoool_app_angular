from rest_framework import serializers
from .models import *
from .models import Admin

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields ='__all__'