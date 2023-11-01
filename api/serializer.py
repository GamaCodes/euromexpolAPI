from rest_framework import serializers
from .models import dynamicCode

class DynamicSerializer(serializers.ModelSerializer):
    class Meta:
        model=dynamicCode
        fields='__all__'