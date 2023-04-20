from django.db import models

# Create your models here.
class Admin(models.Model):
    admin_id = models.CharField(max_length = 20)
    password = models.CharField(max_length = 30)   

    class Meta:
        db_table = 'admin'
class Teacher(models.Model):
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.BigIntegerField()
    gender = models.CharField(max_length=10)
    dob = models.CharField(max_length=50)
    pic = models.ImageField(upload_to='teacher/')
    password = models.CharField(max_length=50)

    class Meta:
        db_table = 'teachers'


class ClassName(models.Model):
    Class = models.CharField(max_length=10)
    division = models.CharField(max_length=5)
    teacher_name = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null = True )

    class Meta:
        db_table = 'class'