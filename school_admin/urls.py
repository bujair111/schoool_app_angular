from django.urls import path
from . import views

app_name = 'school_admin'


urlpatterns = [
    path('login',views.login),
    path('addteacher', views.add_teacher)
]