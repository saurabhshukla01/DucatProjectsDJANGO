from django.shortcuts import render,redirect
from .forms import *
# Create your views here.

def index(request):
    if request.method=='POST':
        regform=Regform(request.POST)
        profile_form=Profileform(request.POST)
        if  regform.is_valid() and profile_form.is_valid():
            regform.save()
            u=User.objects.get(username=regform.cleaned_data['username'])
            f=profile_form.save(commit=False)
            f.user=u
            f.save()
            return redirect('home')
            
    else:
        regform=Regform()
        profile_form=Profileform()
    return render(request,'home.html',{'regform':regform,
                                        'profile_form':profile_form})       
        

def home(request):
    p=Profile.objects.all()
    return render(request,'home1.html',{'p':p})
