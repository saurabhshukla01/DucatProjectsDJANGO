from django.shortcuts import render,HttpResponse, redirect
from .forms import Restroregis,Restromenuform
from django.contrib.auth.models import User
from .models import Restromenudb
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,'home.html')

def addrestrofun(request):
    if request.method=='POST':
        obj=Restroregis(request.POST)
        if obj.is_valid():
            User_Name=obj.cleaned_data['User_Name']
            Restaurant_Name=obj.cleaned_data['Restaurant_Name']
            Email=obj.cleaned_data['Email']
            Password=obj.cleaned_data['Password']
            User.objects.create_user(username=User_Name,first_name=Restaurant_Name,email=Email,password=Password)
            return HttpResponse('<h1>Data Saved</h1>')
        else:
            return HttpResponse('Invalid Entry')
    else:
        obj=Restroregis()
        return render(request,'addrestro.html',{'restroregiskey':obj})

def loginrestro(request):
    if request.method=='POST':
        uname=request.POST['username']
        pssword=request.POST['password']
        user=authenticate(username=uname,password=pssword)
        if user is not None:
            login(request,user)
            return redirect('showrestrofun')
        else:
            return HttpResponse('<h1>INVALID</h1>')
    else:
        return render(request,'home.html')

def showrestro(request):
    obj=User.objects.all()
    return render(request,'show.html',{'showobj':obj})
def showrestro1(request):
    obj=User.objects.all()
    return render(request,'showrestro.html',{'showrestroobj':obj})

def additem(request):
    if request.method=='POST':
        obj=Restromenuform(request.POST,request.FILES)
        if obj.is_valid():
            obj.save()
            return redirect('additemform')
    else:
        obj=Restromenuform
        return render(request,'additem.html',{'additemobj':obj})

def showitems(request):
    obj=Restromenudb.objects.all()
    return render(request,'showitem.html',{'showitemobj':obj})