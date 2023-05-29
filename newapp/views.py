from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# from requests import request


# Create your views here.
def login(request):
    if request.method=='POST':
        x=request.POST['username']
        y=request.POST['password']
        user=auth.authenticate(username=x,password=y)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credential")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        x=request.POST['username']
        y=request.POST['first_name']
        a=request.POST['last_name']
        b=request.POST['email']
        c=request.POST['password']
        d=request.POST['password1']
        if c==d:
            if User.objects.filter(username=x).exists():
                messages.info(request,"username already taken")
                return redirect('register')
            elif User.objects.filter(email=b).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            else:
              e=User.objects.create_user(username=x,password=c,first_name=y,last_name=a,email=b)
              e.save();
              return redirect('login')
              # print("user created")
        else:
           messages.info(request,"password not matched")
           return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')