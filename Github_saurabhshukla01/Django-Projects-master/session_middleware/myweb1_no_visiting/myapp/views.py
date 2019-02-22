from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .forms import *

# Create your views here.
# 8171066647
def index(request):
    
    #a=Info.objects.all()[:3]
    a=Info.objects.order_by('-first_name')[:]
    num_visit = request.session.get('num_visit',1)
    print(num_visit)
    request.session['num_visit']=num_visit+1
    return render(request,'home.html',{'record':a,'nv':num_visit})

def contact(request):
    
    if request.method == "POST":
        form = contactform(request.POST)
        if form.is_valid():
            
            con_obj=Info(first_name=form.cleaned_data['first_name']
                            ,last_name=form.cleaned_data['last_name'],
                        )

            con_obj.save()
            
            return HttpResponseRedirect('/success/')
            
    else:
        form=contactform()
    return render(request,'contact.html',{'form':form})

def success(request):
    return render(request,'success.html')

def detail(request,d,name):
    n=Info.objects.get(id=d)
    return render(request,'detail.html',{'t':n})

def delete_record(request,e):
    n=Info.objects.get(id=e)
    n.delete()
    return HttpResponse('deleted')
