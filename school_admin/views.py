from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
 

@api_view(['POST'])
def login(request):
    
    params = request.data
    username = params['admin_id']
    password = params['password']
     
    try:
        admin=Admin.objects.get(admin_id = username,password = password)
        
        return JsonResponse ({'statusCode': 201, 'token': 'school_admin', 'adminId':admin.id,})
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

@api_view(['GET'])
def view_teacher(request):
    print('heloo')
    try:
        teachers_list = Teacher.objects.all()
        serialized_list = TeacherSerializer(teachers_list, many = True)
        return JsonResponse({'teachers': serialized_list.data, 'statusCode': 200, 'msg': "oky" })
    except Exception as a:
        print(a)
        return JsonResponse({'teachers': [], 'statusCode': 505, 'msg': "Something Went Wrong"})


@api_view(['POST'])
def addclass(request):
   
    msg =''
    try:
        params = request.data
        print(request.data)
        classes = ClassSerializer(data = params)
        if classes.is_valid():
            classes.save()
            statusCode = 204
            msg = 'class added'
        else:
            statusCode = 403
            msg = 'form error'
            print(classes.errors)
            
    except:
            statusCode =505
            msg = 'something went wrong'
    return JsonResponse({'statusCode': statusCode, 'msg': msg})


@api_view(['GET'])
def classlist(request):
    try:
        classes = ClassName.objects.all()
        serialized_classes = ClassSerializer(classes, many=True)
        return JsonResponse({'classes':serialized_classes.data, 'statusCode': 200, 'msg': 'oky'})
    except:
        return JsonResponse({'classes': [], 'statusCode': 505, 'msg': "Something Went Wrong"})


@api_view(['DELETE'])
def delete_class(request,classId):
    try:
        selected_class = ClassName.objects.get(id = classId)
        selected_class.delete()
        return JsonResponse({'msg': 'class deleted', 'statusCode': 204})
    except:
        return JsonResponse({'msg': 'something went wrong', 'statusCode': 505})


def test(request):
    pass