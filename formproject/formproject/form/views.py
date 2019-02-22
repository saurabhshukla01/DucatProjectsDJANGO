from django.shortcuts import render, HttpResponse, redirect
from .forms import *
from .models import *
from django.contrib import messages


def index(request):
    form = NameForm()
    return render(request, 'index.html', {"form1":form})

def home(request):
    if request.method=="POST":
        obj  = StudentForm(request.POST,request.FILES)
        if obj.is_valid():
            obj.save()
            messages.success(request,"Student Data Inserted.")
            return redirect('show')
        else:
            return HttpResponse("ERROR")    
    studentform = StudentForm()
    return render(request,'student.html', {"student":studentform})

def showdata(request):
    data = Student.objects.all()
    return render(request, 'show.html',{"students":data})