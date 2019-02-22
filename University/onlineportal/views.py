from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from University import settings
from django.template.loader import render_to_string
from .models import *   
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator



# Create your views here.
@login_required(login_url="/login")
def addUniversity(request):  
    if request.method == "POST":  
        form = UniversityForm(request.POST,request.FILES)  
        if form.is_valid():  
            form.save()  
            return redirect('/')            
    else:  
        form = UniversityForm()  
    return render(request,'university.html',{'form':form})  



def addproff_of_university(request):  
    if request.method == "POST":  
        form = proffForm(request.POST,request.FILES)  
        if form.is_valid():  
            form.save()  
            return redirect('/')               
    else:  
        form = proffForm()  
    return render(request,'proff.html',{'form':form})


def showproff_details(request):
    if request.method == "POST":  
        form = proff_details_Form(request.POST,request.FILES)  
        if form.is_valid():  
            form.save()  
            return redirect('/')               
    else:  
        form = proff_details_Form()  
    return render(request,'proff_details.html',{'form':form})
  

def homepage(request):
    if request.user.is_authenticated:
        return Universitylist(request)
    else:
        return AppForm(request) 


def AppForm(request):
    if request.method=="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            Address = form.cleaned_data['Address']
            Parents_name = form.cleaned_data['Parents_name']
            age = form.cleaned_data['age']
            contact_no = form.cleaned_data['contact_no']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username,
			first_name=first_name,last_name=last_name,
            password=password)
            subject="Confirmation Mail"
            msg="Dear Sir/Ma'am,thank YOU FOR MORE DETAILS CONTACT VISIT UNIVERSITY AND PROFF__DETAILS PROFF__NAMES....:"
            message = render_to_string('mail_templates_confirm.html')
            send_mail(subject,msg,settings.EMAIL_HOST_USER,[email],
                    html_message=message)
            messages.success(request, 'Data is Entered')
            return redirect('register')
    else:    
        form = RegistrationForm()                                                     
    return render(request, 'registration.html', {'form':form})


def loginuser(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            
            return redirect('university')
            #return HttpResponse ('<h1>Logged In</h1>')
        else:
            return render(request, 'login.html',{'name':username})
            #return HttpResponse('<h1>invalid</h1>') 
    return render(request, 'login.html')


def logoutuser(request):
	logout(request)
	return render(request,'login.html')


def Universitylist(request):
    University_list = University.objects.get_queryset().order_by('-id')
    paginator = Paginator(University_list, 2)
    page = request.GET.get('page')
    university = paginator.get_page(page)
	#?page = 2
    context={"Universities":university}
    print(paginator.page_range)
    #data = University.objects.all()
    return render(request,'universitylist.html',{'Universities':university})


def Universitydetail(request, id):
    data = University.objects.filter(id=id)
    print(data)
    return render(request, 'university_detail.html',{'profflist':data})


def index_proffdetail(request):
    if request.user.is_authenticated:
        return profflist(request)
    else:
        return AppForm(request) 


def profflist(request):
    proff_list = proff_of_university.objects.get_queryset().order_by('-id')
    print(proff_list)
    paginator = Paginator(proff_list, 2)
    page = request.GET.get('page')
    proff = paginator.get_page(page)
	#?page = 2
    context={"proff_of_universites":proff}
    print(paginator.page_range)
    #data = proff_of_university.objects.all()
    return render(request,'profflist.html',{"proff_of_universites":proff})


def proff_details1(request, id):
    data = proff_details.objects.filter(proff_details_id=id)
    print(data)
    return render(request, 'proff_details.html',{'proffdetail':data})


def proffdetaillist(request):
    proffdetail_list = proff_details.objects.get_queryset().order_by('-id')
    paginator = Paginator(proffdetail_list, 2)
    page = request.GET.get('page')
    proff = paginator.get_page(page)
	#?page = 2
    context={"proff_detailss":proff}
    print(paginator.page_range)
    #data = proff_details.objects.all()
    return render(request,'proffdetaillist.html',{"proff_detailss":proff})


def proff_detaillist(request, id):
    print(proff_details.objects.all())
    data = proff_details.objects.get_queryset().order_by('-id')

    return render(request, 'proffdetailshow.html',{'proffdetaillist':data})



def index_proffdetaillist(request):
    if request.user.is_authenticated:
        return proffdetaillist(request)
    else:
        return AppForm(request) 