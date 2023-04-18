from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TeacherSerializer
 

@api_view(['POST'])
def login(request):
    
    params = request.data
    username = params['admin_id']
    password = params['password']
     
    try:
        Admin.objects.get(admin_id = username,password = password)
         
        return JsonResponse ({'statusCode': 201, 'token': 'school-admin'})
    except :
        
        return JsonResponse ({'statusCode': 404})

@api_view(['POST'])
def add_teacher(request):
    msg = ''
    try:
        params = request.data

        teacher_data = TeacherSerializer(data = params)

        if teacher_data.is_valid():
            teacher_data.save()
            msg = "Teacher Added"
            statusCode = 204
        else:
            msg = 'Form Error'
            statusCode = 403
    except:
        msg = 'Something went wrong'
        statusCode = 505
    return JsonResponse({'statusCode' : statusCode, 'msg' : msg})

    