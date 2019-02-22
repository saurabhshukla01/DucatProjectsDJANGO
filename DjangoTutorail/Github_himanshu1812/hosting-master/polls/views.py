from django.shortcuts import render, redirect, HttpResponse
from .forms import EmployeeForm, userform, ChangePasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
	TemplateView, 
	CreateView, 
	ListView,
	UpdateView,
	DeleteView,
	)

'''
def showdata(request):
	profile_list = Employee.objects.get_queryset().filter(eage__gte=20).order_by('eage')
	#profile_list = Employee.objects.all()
	paginator = Paginator(profile_list, 4)
	page = request.GET.get('page')
	employee = paginator.get_page(page)
	#?page = 2
	context={"employees":employee}
	#print(paginator.page_range)
	return render(request,'show.html',context)
'''



def showsession(request):
	num_visit = request.session.get('num_visit',1)
	request.session.set_expiry(100) 
	print(num_visit)
	request.session['num_visit']=num_visit+1
	return render(request,'show.html',{'nv':num_visit})
	
class EmployeeListView(ListView):
	template_name = 'show.html'
	model = Employee
	paginate_by = 4
	
	def get_context_data(self):
		context = super().get_context_data()
		context['college_list'] = College.objects.all()
		context['student_list'] = Student.objects.all()
		return context

class Collegedelete(DeleteView):
	model = College
	success_url = "/show"
	template_name = 'polls/employee_confirm_delete.html'
	
class Employeeupdate(SuccessMessageMixin,UpdateView):
	model = Employee
	form_class = EmployeeForm	
	success_message = 'Profile has been Updated'	

class Employeedelete(DeleteView):
	model = Employee
	success_url = "/show"
	
class Home(TemplateView):
	template_name = 'index.html'

def changepassword(request):
    user=request.user
    if request.method == "POST":
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password=form.cleaned_data['new_password']
            user.set_password(new_password)
            user.save()            
            return redirect('/login')
    else:
        form = ChangePasswordForm()
    return render(request,'changepass.html', {'form':form})	
	
def index(request):
	if request.user.is_authenticated:
		return render(request, 'index.html')
	else:
		return redirect('/login')

# Create your views here.
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
			subject="Confirmation Mail"
			msg="Dear Sir/Ma'am,thank YOU FOR MORE DETAILS CONTACT VISIT:"
			send_mail(subject,msg,settings.EMAIL_HOST_USER,[email])
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
