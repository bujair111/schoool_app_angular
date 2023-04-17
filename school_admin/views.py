from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
 

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
