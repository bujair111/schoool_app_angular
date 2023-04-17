from django.db import models

# Create your models here.
class Admin(models.Model):
    admin_id = models.CharField(max_length = 20)
    password = models.CharField(max_length = 30)   

    class Meta:
        db_table = 'admin'