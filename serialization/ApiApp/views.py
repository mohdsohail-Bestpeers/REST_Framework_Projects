from django.shortcuts import render
from .models import student
from .serializers import stuSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

def student_details(request,pk):
    stu=student.objects.get(id=pk)           #complex data type
    #print(stu)
    serializer=stuSerializer(stu)           #python native datatype    
    #print(serializer)
    #print(serializer.data)
    json_data= JSONRenderer().render(serializer.data)     #render into json
    #print(json_data)
    return HttpResponse(json_data, content_type='application/json')
    #return HttpResponse(json_data, content_type='application/x-javascript')
    #return HttpResponse(json_data, content_type='text/javascript')
    #return HttpResponse(json_data, content_type='text/x-javascript')
    #return HttpResponse(json_data, content_type='text/x-json')
    
#query set - all student data    
def student_list(request):
    stu=student.objects.all()
    serializer=stuSerializer(stu, many=True)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
    