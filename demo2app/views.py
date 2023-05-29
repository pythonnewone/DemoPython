from django.http import HttpResponse
from django.shortcuts import render
from.models import place
from.models import members
# Create your views here.
def fun(request):
    obj=place.objects.all
    obj1=members.objects.all
    # name="India"
    return render(request,"index.html",{'result':obj,'result1':obj1})
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,"result.html",{'value':res})
# def about1(request):
#     return render(request,"about1.html")
# def contact(request):
#     return HttpResponse("hello am contact")
