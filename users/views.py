from django.shortcuts import render,redirect

#Django
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect("inicio")
        else:
            return render(request,"users/login.html",{"error": "Usuario o contraseña invalido"})
    
    return render(request,'users/login.html');

@login_required
def logout_view(request):
    logout(request)
    return redirect('inicio')