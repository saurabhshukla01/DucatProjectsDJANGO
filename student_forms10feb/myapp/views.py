from django.shortcuts import render, redirect, HttpResponse
from .forms import student_form
from django.contrib import messages
from django.contrib.auth.models import User


def student1(request):
    if request.method == 'POST':
        form = student_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration succesfully.')
            return HttpResponseredirect('studentform/')

    else:
        form = student_form()
        #messages.success(request, 'Registration succesfully.')
    return render(request,'student.html',{'form':form})



# Create your views here.
