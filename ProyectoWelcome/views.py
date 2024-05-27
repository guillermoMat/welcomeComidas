from django.http import HttpResponse
from datetime import datetime

from django.shortcuts import render


def hello_word(request):
    listNumeros=request.GET['numbers']
    return HttpResponse(   "Bienvenidos {}".format(str(listNumeros)) )

def say_hi(request,name,age):
    if age<18:
        messagge="Lo siento {}, es menor de edad.".format(name)
    else:
        messagge="Bienvenido {} al mundo Python.".format(name)
    
    return HttpResponse(messagge)

