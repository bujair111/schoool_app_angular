from django.urls import path
from . import views

app_name = 'teacher'


urlpatterns = [
    path('login',views.login),
]