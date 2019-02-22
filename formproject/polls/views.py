from django.shortcuts import render, redirect, HttpResponse
from .forms import EmployeeForm, userform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.decorators import login_required
from .models import *

class Home(TemplateView):
	template_name = 'index.html'

def index(request):
	if request.user.is_authenticated:
		return render(request, 'index.html')
	else:
		return redirect('/login')

# Create your views here.
#@login_required(login_url='/login')
class EmployeeData(CreateView):
	model = Employee
	form_class = EmployeeForm
	
	
def registration(request):
	if request.method=='POST':
		form1=userform(request.POST)
		if form1.is_valid():
			uname=form1.cleaned_data['username']
			first_name = form1.cleaned_data['first_name']
			last_name = form1.cleaned_data['last_name']
			email = form1.cleaned_data['email']
			password = form1.cleaned_data['password']
			User.objects.create_user(username=uname,
			first_name=first_name,last_name=last_name,
			email=email,password=password)
			return redirect('/employeeform')
	else:
		form1=userform()
	return render (request, 'registration.html',{'form':form1})
	
def login_user(request):
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return render(request, 'index.html')
		else:
			return HttpResponse('<h1>invalid</h1>')
	return render(request, 'login.html')	
#pip install django-crispy_forms    
def logout_user(request):
	logout(request)
	return render(request,'login.html')    
