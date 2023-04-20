from rest_framework import serializers
from .models import *
from .models import Admin

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields ='__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields ='__all__'

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassName
        fields =('id','Class','division')        