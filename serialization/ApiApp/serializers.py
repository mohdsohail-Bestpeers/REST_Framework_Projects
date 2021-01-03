from rest_framework import serializers


class stuSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50)
    role=serializers.IntegerField()
    city=serializers.CharField(max_length=50)