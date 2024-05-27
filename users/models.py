from django.db import models



# Create your models here.
class User(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=253)
    fullname = models.CharField(max_length=100)