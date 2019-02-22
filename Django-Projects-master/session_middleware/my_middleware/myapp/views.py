from django.shortcuts import render
from django.http import *

# Create your views here.
def index(request):
    #print request
    return HttpResponse('hi')
