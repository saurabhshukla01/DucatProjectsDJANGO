from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import *
from django.contrib import auth
from django.contrib.auth import REDIRECT_FIELD_NAME
# Create your views here.
from .forms import *
from django.contrib.auth.models import User
from .decorators import *
from django.db.models import Q


def login(request):
    redirect_to = REDIRECT_FIELD_NAME
    r=request.GET.get(redirect_to)
    #r=request.GET.get('next1')
    print r
    if r is None:
        r='/'
    if request.method=='POST':

        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
         
        if user is not None:
            auth.login(request,user)
            
            return HttpResponseRedirect(r)
        else:
            return HttpResponseRedirect('/invalid/')
        
    
    return render(request,'login.html')


def index(request):

    if request.method=='POST':
        form =Postform(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.created_by=request.user
            f.save()
            return HttpResponseRedirect('/')
    
    else:
        form=Postform()
        posts=Post.objects.order_by('-id')
        all_share_post = SharePost.objects.all()
        #pro = Profile.objects.get(user=request.user)
    return render(request,'home.html',{'form':form,
                                       'posts':posts,
                                       'all_share':all_share_post})

def home(request):
    if request.user.is_authenticated():
        return index(request)
    else:
        return login(request)
'''
def auth_view(request):
    
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username,password=password)
     
    if user is not None:
        auth.login(request,user)
        
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/invalid/')
'''    

def invalid_login(request):
    return render(request,'invalid_login.html')

@login_required(login_url='/')
@user_authenticate
def edit(request,d):
    record=Post.objects.get(id=d)
    if request.method=='POST':
        form =Postform(request.POST,instance=record)
        if form.is_valid():
            f=form.save(commit=False)
            f.created_by=request.user
            f.save()
            return HttpResponseRedirect('/')
    
    else:
        form=Postform(instance=record)
       
    return render(request,'edit.html',{'form':form})

@login_required(login_url='/')
@user_authenticate
def delete(request,d):
    try:
        n=Post.objects.get(id=d)
    except:
        return HttpResponse('Try Again....!')
    n.delete()
    return HttpResponseRedirect('/')

def logout(request):
    auth.logout(request)
    #return render(request,'login.html')
    return HttpResponseRedirect('/')

def signup(request):
    if request.method=='POST':
        form=Regforms(request.POST,request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, password=password,
                                     email=email)
            obj=Profile(user=User.objects.get(username=username),
                        pic=form.cleaned_data['pic'])
            obj.save()
            return HttpResponseRedirect('/')
            #user = authenticate(username=username, password=password)
            #login(request, user)
            #return render(request,'login.html')
    else:
        form=Regforms()
    return render(request,'signup.html',{'form':form})

@login_required(login_url='/')
def detail(request,d):
    n=Post.objects.get(id=d)
    return render(request,'detail.html',{'n':n})
    
    
def share_post(request,d):
    u=User.objects.all()

    u=u.exclude(Q(id=request.user.id)| Q(is_staff=True))
   
    return render(request,'share.html',{'all_user':u,
                                        'post_id':d})


def sharepost(request,d,post_id):
    u=User.objects.get(id=d)
    post=Post.objects.get(id=post_id)
    t=SharePost()
    t.user=u
    t.post=post
    t.save()
    return HttpResponseRedirect('/')








