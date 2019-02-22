from django.shortcuts import render
from datetime import *
from .models import *
from .forms import *
from django.http import *

# Create your views here.

def index(request):
    pub_list = Publisher.objects.all()

    c= Book.objects.all()

    for k in c:
        print 'book name:',k.title
        print 'pub name:',k.publisher.name
        print 'pub address:',k.publisher.address
    return render(request,'home.html',{'pub_list':pub_list})


def Pub_form(request):
    if request.method == 'POST':
        form = Publisherform(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')

    else:
        form = Publisherform()
        
    return render(request,'pubform.html',{'form':form})


def book_form(request):
    if request.method == 'POST':
        form = Bookform(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')

    else:
        form = Bookform()
        
    return render(request,'bookform.html',{'form':form})
