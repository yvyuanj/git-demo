from django.db import models
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=2)
    #data = models.IntegerField()


class Department(models.Model):
    title = models.CharField(max_length=16)

class Role(models.Model):
    caption = models.CharField(max_length=16)
# Create your models here.









#python manage.py makemigrations
#python manage.py migrate