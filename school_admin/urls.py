from django.urls import path
from . import views

app_name = 'school_admin'


urlpatterns = [
    path('login',views.login),
    path('addteacher', views.add_teacher),
    path('teachers/list', views.view_teacher),
    path('addclass', views.addclass),
    path('class/list', views.classlist),
    path('class/delete/<int:classId>', views.delete_class)

]