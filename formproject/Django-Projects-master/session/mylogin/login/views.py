from django.shortcuts import render,redirect
from django.http import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required
#from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User



def login(request):
    #request.COOKIES['sessionid']=ses_id
    return render(request,'login.html')

def auth_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        request.session.save()
        print request.COOKIES
        
        #ses_id=request.COOKIES['sessionid']
        #print ses_id
        
        session_key=request.session.session_key
        #print session_key
        
        session = Session.objects.get(session_key=session_key)
        print 'session:',session
        print session.get_decoded()
        uid = session.get_decoded().get('_auth_user_id')
        user = User.objects.get(pk=uid)

        print 'username:',user.username
        
        request.session['user_id']=user.id
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')
    

def loggedin(request):
    if request.user.is_authenticated():
        return render(request,'loggedin.html',{'fullname':request.user.username})
    else:
        return redirect('/')

    
def invalid_login(request):
    return render(request,'invalid_login.html')

def logout(request):
    
    #del request.session['user_id']
   
   
    auth.logout(request)
    return HttpResponseRedirect('/')
        
    
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success/')

    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})    


def register_success(request):
    return render(request,'register_success.html')
    


