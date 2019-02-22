from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'home.html')

def departments(request):
    return render(request,'departments.html')

def academics(request):
    return render(request,'Academics.html')

def directorate(request):
    return render(request,'Directorate.html')

def deans(request):
    return render(request,'Deans.html')

def palacements(request):
    return render(request,'Palacements.html')

def campus(request):
    return render(request,'Campus.html')

def centres(request):
    return render(request,'centres.html')

def contact(request):
    return render(request,'Contact.html')

def quicklinks(request):
    return render(request,'Quciklinks.html')