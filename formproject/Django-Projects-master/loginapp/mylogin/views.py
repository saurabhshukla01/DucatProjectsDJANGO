from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import auth
from django.contrib.auth import authenticate, login
from .models import *
from django.db.models import Q
from django.contrib import messages

def login(request):
    return render(request,'login.html')

def index(request):
    
    if request.method=='POST':
        
        form = Postform(request.POST,request.FILES)
        if form.is_valid():
            obj=Post(user=request.user,
                    
                     content=form.cleaned_data['content'],
                     pic=form.cleaned_data['pic'])
            obj.save()
            return redirect('home')
    else:
        form=Postform()
        data=Post.objects.all()
        comts=comment.objects.all()
       
        
            
    return render(request,'home.html',{'form':form,
                                       'comts':comts,'data':data})
    
    
def home(request):
    if request.user.is_authenticated():
        return index(request)
    else:
        return login(request)
    
def auth_view(request):
    
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/invalid/')    
def signup(request):
    if request.method=='POST':
        form=Regforms(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password,
                                     email=email)
            user = authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect('/')
    else:
        form=Regforms()
    return render(request,'signup.html',{'form':form})    

def delete(request,d):
    n=Post.objects.get(id=d)
    n.delete()
    return redirect('post')

def logout(request):
    auth.logout(request)
    return render(request,'login.html')    

def user_profile(request):
    user=request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.profile.job_title = form.cleaned_data.get('job_title')
            user.email = form.cleaned_data.get('email')

            user.profile.location = form.cleaned_data.get('location')
            user.profile.pic = form.cleaned_data.get('pic')
            user.save()
            
            
            return redirect('post')

    else:
        form = ProfileForm(instance=user, initial={
            'job_title': user.profile.job_title,
            'location': user.profile.location,
            'pic':user.profile.pic
            })
    return render(request,'profile.html',{'form':form})    

def search(request):
    if request.method =='POST':

        squery = request.POST['search_box']
        if squery:
            
            form=Postform()
            s = Post.objects.filter(Q(title__icontains=squery)|Q(content__icontains=squery)|Q(user__first_name__exact=squery))
            if s:
                return render(request,'search.html',{'data':s})
            else:
                return render(request,'home.html',{'form':form,'msg':
                                                   'Record not found'})
            
        else:    

            return HttpResponseRedirect('/posts/')

    else:
        pass
    return render(request,'search.html')

def password(request):
    user=request.user
    if request.method == "POST":
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password=form.cleaned_data['new_password']
            user.set_password(new_password)
            user.save()
            
            return redirect('login')

    else:
        form = ChangePasswordForm()
    return render(request,'password.html',{'form':form}) 

def comments(request):
    if request.method == 'POST':
        post_id = request.POST['feed']
        post_obj = Post.objects.get(id=post_id)
        #post = request.POST['post']
        #post = post.strip()
        form=comment_form(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.post=post_obj
            f.cmt_user=request.user
            f.save()
            return redirect('home')
    else:
        form=comment_form()
            
            
    result=Post.objects.all()
    return render(request,'home.html',{'form':form,'data':result})   