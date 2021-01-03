from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import student
from .serializers import stuSerializer


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request, pk):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = student.objects.get(id=id)
            serializer = stuSerializer(stu)
            return Response(serializer.data)
        stu = student.objects.all()
        serializer = stuSerializer(stu, many=True)
        return Response(serializer.data)


    if request.method == 'POST':
        serializer = stuSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data posted'})
        return Response(serializer.errors)


    if request.method == 'PUT':
        id = pk
        stu = student.objects.get(pk=id)
        serializer = stuSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'compleate data updated!!'})
        return Response(serializer.errors)


     if request.method == 'PATCH':
        id = pk
        stu = student.objects.get(pk=id)
        serializer = stuSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial data updated!!'})
        return Response(serializer.errors)



    if request.method == 'DELETE':
        id = pk
        stu = student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'data deleted!!'})
    