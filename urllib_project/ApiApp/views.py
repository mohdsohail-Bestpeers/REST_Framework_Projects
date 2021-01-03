from django.shortcuts import render
import requests
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import StudentSerializer
from .models import Student
from django.http import HttpResponse
from .forms import StudentForm
import urllib3
import json

'''GET method '''
def student(request):
    http = urllib3.PoolManager()
    response = http.request('GET', 'http://127.0.0.1:8000/list/')
    print(response.data)
    response = json.loads(response.data.decode())
    # response = requests.get("http://127.0.0.1:8000/list/").json()
    return render(request, 'home.html', {'response':response})

class studentapi(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


'''POST method'''
def student_form(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            roll = form.cleaned_data['roll']
            info = {'name':name, 'roll':roll}
            http = urllib3.PoolManager()
            response = http.request('POST', 'http://127.0.0.1:8000/formapi/', fields=info)
            # response = requests.post("http://127.0.0.1:8000/formapi/", data=info)
            return HttpResponse("ok")
    return render(request, 'form.html', {'form':form})

class studentformapi(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


'''UPDATE method'''
def student_update(request, id):
    obj = Student.objects.get(id=id)
    form1 = StudentForm(instance=obj)
    if request.method == 'POST': 
        obj = Student.objects.get(id=id)
        form1  = StudentForm(request.POST, instance=obj)
        if form1.is_valid():
            name = form1.cleaned_data['name']
            roll = form1.cleaned_data['roll']
            info = {'name':name, 'roll':roll}
            url  = "http://127.0.0.1:8000/updateapi/" + str(id) + '/'
            http = urllib3.PoolManager()
            response = http.request('PUT', url, fields = info)
            # response = requests.post("http://127.0.0.1:8000/formapi/", data=info)
            return HttpResponse("ok")
    return render(request, 'form.html', {'form':form1})

class studentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


'''DELETE method'''
def student_delete(request, id):
    url = "http://127.0.0.1:8000/deleteapi/" + str(id) + '/'
    http = urllib3.PoolManager()
    response = http.request('DELETE', url)
    return HttpResponse('Deleted Sucessfully')   

class studentDelete(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

