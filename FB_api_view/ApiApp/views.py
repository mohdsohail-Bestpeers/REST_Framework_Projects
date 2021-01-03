from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# @api_view()
# def student_welcome(request):
#     return Response({'msg':'welcome my student'})


# @api_view(['POST'])
#this is use for post method
# def post(request):
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg':'this is POST request'})



@api_view(['GET','POST'])
#this is use for both POST and GET method
def post(request):
    if request.method == 'GET':
        return Response({'msg':'this is get method'})

    if request.method == 'POST':
        print(request.data)
        return Response({'msg':'this is POST request','data':request.data})