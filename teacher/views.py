from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from school_admin.models import Teacher


@api_view(['POST'])
def login(request):
    try:
        
        params = request.data
        teacher_id = params['teacher_id']
        password = params['password']
        try:
            teacher_id = Teacher.objects.get(teacher_id = teacher_id , password = password)

            return JsonResponse ({'statusCode': 201, 'token': 'teacher-admin'})


        except:
            return JsonResponse({'statusCode' : 404, 'msg' : 'Incorrect Username or Password'})
    except Exception as e:
        return JsonResponse({'statusCode' : 500 , 'msg' : 'Something Went Wrong'})