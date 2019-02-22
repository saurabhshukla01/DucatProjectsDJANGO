from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.core.mail import send_mail
from emailsender import settings

def home(request):
	if request.method == "POST":  
		form = EmpForm(request.POST)  
		if form.is_valid():  
			try:  
				form.save()  
				subject="Confirmation Mail"
				msg=form.cleaned_data['message']
				to=form.cleaned_data['email']
				res=send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
				return redirect('/thank')  
			except:  
				pass  
	else:  
		form = EmpForm()  
	return render(request,'home.html',{'form':form})  
# Create your views here.
def thank(request):
	return render(request,'thank.html')
def show(request):
	employees = Empl.objects.all()  
	return render(request,'show.html',{'empl':employees})