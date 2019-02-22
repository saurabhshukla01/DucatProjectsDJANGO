from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def home(request):
    return render(request,"home.html")

def student(request):
    return render(request,"student.html")

def csjmu(request):
    return render(request,"csjmu.html")

def data(request):
    return render(request,"data.html")