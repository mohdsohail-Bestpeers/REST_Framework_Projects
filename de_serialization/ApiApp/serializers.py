from rest_framework import serializers
from .models import student

class stuSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 150)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length = 150)
    
    def create(self,validate_data):
        return student.objects.create(**validate_data)
    