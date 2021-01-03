from rest_framework import serializers
from .models import student


'''read_only dont change the name while we udate data'''
class stuSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only = True)
    '''everything will be change but name will not change while updation'''
    class Meta:
        model = student
        fields = ['name','roll','city']
        '''we can use this extra_kwargs also'''
        #extra_kwargs={'name':{'read_only':True}}



'''we can use read_only in multiple fields also.
uncomment this code if you want to use read_only in multiple fields'''
# class stuSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = student
#         fields = ['name','roll','city']
#         read_only_fields = ['name','roll']