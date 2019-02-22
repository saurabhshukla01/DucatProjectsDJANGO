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

def deletestudent(request,id):
    obj = Student.objects.get(id=id)
    print(obj)
    obj.delete()
    messages.success(request,"Student Data Deleted.")
    return redirect('show')

def updatestudent(request,id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':  
        form = StudentForm(request.POST, request.FILES , instance = student)  
        if form.is_valid():  
            form.save()  
            messages.success(request,'Student Updated!!!!!!!')
            return redirect("/show")  
    return render(request, 'updatestudent.html',{'data':student})


def searchstudent(request):
    name = request.POST['searchtext']
    data = Student.objects.filter(name__icontains=name)
    return render(request, 'show.html',{"students":data})