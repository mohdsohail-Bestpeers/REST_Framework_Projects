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


    #field level validation(single field validation)
    def validate_roll(self, value):
        if value>=200:
            raise serializers.ValidationError('seat full')
        return value

    

    #object level validation(multiple field validation)
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'sohail' and ct.lower() != 'indore':
            raise serializers.ValidationError('city must be indore')
        return data


    #validator
    """use this code on the top of the class stuSerializer and update the NAME field same as below"""
    # def start_with_r(value):
    #     if value[0].lower != 'r':
    #         raise serializers.ValidationError('first latter must start with r')
        
    # class stuSerializer(serializers.Serializer):
    # name = serializers.CharField(max_length = 150, validators=[start_with_r])
    # roll = serializers.IntegerField()
    # city = serializers.CharField(max_length = 150)
