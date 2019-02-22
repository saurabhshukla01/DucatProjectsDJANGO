from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth

def register(request):
	if request.method == 'POST':
		form = UserForm(request.POST)

		if form.is_valid():
			username = form.cleaned_data['username']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			return HttpResponse('<h1>Welcome</h1>')
			return render(request,'login.html')
	else:
		form = UserForm()
	return render(request,'register.html',{'form':form}) 

def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return render(request,'index.html')
			#return HttpResponse(f'<h1>Hello {{request.user}}</h1>')
		else:
			return HttpResponse('<h2>Invalid User.</h2>')
	else:
		return render(request,'login.html')

def index(request):
	if request.user.is_authenticated:
		return render(request,'index.html')
	else:
		return redirect('/login')

def logout_user(request):
	logout(request)
	return render(request,'login.html')

def changepassword(request):
	user = request.user
	if request.method == 'POST':
		form = changepasswordform(request.POST)
		if form.is_valid():
			new_password = form.cleaned_data['new_password']
			user.set_password(new_password)
			user.save()
			return redirect('login')
	else:
		form = changepasswordform()
	return render(request,'changepassword.html',{'form':form})

def UserProfile(request):
	User = request.user
	if request.method == 'POST':
		form = ProfileForm(request.POST,request.FILES)
		if form.is_valid():
			User.first_name = form.cleaned_data.get('first_name')
			User.last_name = form.cleaned_data.get('last_name')
			User.Profile.job_title = form.cleaned_data.get('job_title')
			User.email = form.cleaned_data.get('email')
			User.Profile.designation = form.cleaned_data.get('designation')
			User.Profile.location = form.cleaned_data.get('location')
			User.Profile.pic = form.cleaned_data.get('pic')
			User.save()
			return redirect('index')
	else:
		form = ProfileForm(instance=User, initial={'job_title': User.Profile.job_title,'location': User.Profile.location,'pic':User.Profile.pic,'designation':User.Profile.designation})
	return render(request,'profile.html',{'form':form}) 
	
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
    
def post(request):
    
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

def delete(request,d):
    n=Post.objects.get(id=d)
    n.delete()
    return redirect('post')

     

# Create your views here.
