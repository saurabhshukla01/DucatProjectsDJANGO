from django.shortcuts import *
from django.http import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User



def login(request):
    return render(request,'login.html')


def auth_view(request):
    #print request.POST['username']
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        
        return HttpResponseRedirect('/logged_in/')
    else:
        return HttpResponseRedirect('/invalid/')
    
def loggedin(request):
    if request.user.is_authenticated():
        return render(request,'loggedin.html',{'fullname':request.user.username})
    else:
        return HttpResponseRedirect('/')
    
    
def invalid_login(request):
    return render(request,'invalid_login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
        
    
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        #print form['username']
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_success/')

    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})    


def register_success(request):
    return render(request,'register_success.html')
    


