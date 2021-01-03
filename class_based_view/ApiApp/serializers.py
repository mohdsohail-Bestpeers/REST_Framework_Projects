from rest_framework import serializers
from .models import student


class stuSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 150)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length = 150)


    #using create method
    def create(self, validate_data):
        return student.objects.create(**validate_data)
    

    #using update method
    def update(self,instance, validate_data):
        #new data from user for update is known as "validate_data"
        #old data is stored in database is known as "instance"
        print(instance.name)
        instance.name=validate_data.get('name',instance.name)
        print(instance.name)
        instance.roll=validate_data.get('roll',instance.roll)
        instance.city=validate_data.get('city',instance.city)
        instance.save()
        return instance