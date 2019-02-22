from django.shortcuts import render
from .models import *
# Create your views here.
from .forms import *
from django.http import *

def index(request):
    info=Emp.objects.all()
    return render(request,'home.html',{'info':info})

def user_form(request):
    if request.method=='POST':
        form = Myform(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            obj=User(username=cd['username'],
                     email=cd['email'])
            obj.save()
            Emp.objects.create(user=obj,department=cd['department'])
            
            
            return HttpResponseRedirect('/')
    else:
        form = Myform()
    return render(request,'form.html',{'form':form})
