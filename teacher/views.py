from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from school_admin.models import Teacher


@api_view(['POST'])
def login(request):
    try:
        
        params = request.data
        email = params['email']
        password = params['password']

        try:
            teacher = Teacher.objects.get(email = email , password = password)
            return JsonResponse ({'statusCode': 201, 'token': 'teacher_token','teacherId': teacher.id, 'teacherName': teacher.name})
        except Exception as e:
            print(e)
            return JsonResponse({'statusCode' : 404, 'msg' : 'Incorrect Username or Password'})
        
    except :
        return JsonResponse({'statusCode' : 500 , 'msg' : 'Something Went Wrong'})