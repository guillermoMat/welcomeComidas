from datetime import date
from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    website=models.URLField(max_length=200, blank=True)
    biografia=models.TextField(blank=True)
    phone_number=models.CharField(max_length=20, blank=True)

    #para utilizar ImageField debes instalar la libreria "pillow"
    #desde consola/proyecto con el "venv" activado
    #pip install pillow

    #picture=models.ImageField(upload_to="carpetaAplicacion/carpetadondeestalaimagen",
     #                         blank=True, null=True)
    
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.user.username