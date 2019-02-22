from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def ApplicationForm(request):
    if request.method=="POST":
        form = Addharform(request.POST)
        if form.is_valid():
            
            Name=form.cleaned_data['Name']
            Email = form.cleaned_data['Email']
            DOB = form.cleaned_data['DOB']
            Gender = form.cleaned_data['Gender']
            Address = form.cleaned_data['Address']
            Parents_name = form.cleaned_data['Parents_name']
            Mob_no = form.cleaned_data['Mob_no']
            
            User.objects.create_user(Name=Name,
			Email=Email,DOB=DOB,Gender=Gender,
            Address=Address,Parents_name=Parents_name,
            Mob_no=Mob_no)

            messages.success(request, 'Data is Entered')
            return redirect('application')
    else:    
        form = Addharform()
    return render(request, 'application.html', {'form':form})



# Create your views here.
