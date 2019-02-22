from django.shortcuts import render
from django.http import *
from mylogin.models import *
from mylogin.forms import *
from django.db.models import Q

# Create your views here.

def search_new(request):
    if 'q' in request.GET:
        squery = request.GET.get('q').strip()
        
        if squery:
            form=Postform()
            s = Post.objects.filter(Q(content__icontains=squery)|
                                    Q(user__first_name__iexact=squery)|
                                    Q(user__profile__location__icontains=squery)|
                                    Q(user__profile__job_title__icontains=squery)|
                                    Q(user__last_name__iexact=squery)|
                                    Q(user__username__iexact=squery))
            if s:
                 return render(request,'home.html',{'form':form,'data':s,'q':squery})

            else:
                return render(request,'home.html',{'form':form,'no_result':True})
                
        else:
            return HttpResponseRedirect('/')
