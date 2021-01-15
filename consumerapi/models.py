from django.db import models

# Create your models here.


class Logininfo(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30, unique=True)
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=30,unique=True)
    active = models.CharField(max_length=10,default='Y')
    role = models.CharField(max_length=10,default= 'G')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Login'



