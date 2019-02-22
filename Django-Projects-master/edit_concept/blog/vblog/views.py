from django.shortcuts import render,get_object_or_404
from django.http import *
from .forms import *
from .models import *
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

global fullname

fullname=''

def index(request):
    #post_obj = Post.objects.all().order_by('-timestamp')
    contact_list = Post.objects.all()
    paginator = Paginator(contact_list, 3) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        post_obj = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        post_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        post_obj = paginator.page(paginator.num_pages)
    return render(request,'post_list.html',{'list':post_obj})



def login(request):
    return render(request,'login.html')


def logout_page(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def search(request):
    if request.method =='POST':

        
        squery = request.POST.get('search_box', None)
        s = Post.objects.filter(Q(title__icontains=squery) | Q(content__icontains=squery ))
        if s:
            return render(request,'post_search.html',{'q':s})
        else:
            return render(request,'post_notfound.html')
            
            
    return render(request,'post_search.html',{'q':s})    
    #return HttpResponse(squery)

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/postcreate/')
    else:
        return HttpResponseRedirect('/accounts/invalid')
'''
def loggedin(request):
    if request.user.is_authenticated():
        return render(request,'loggedin.html',{'fullname':request.user.username})
    else:
        return HttpResponse('/')
 '''   


def post_create(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            fullname=request.user.username
            title=request.POST.get('title')
            content=request.POST.get('content')
            image=form.cleaned_data['image']
            post_con = Post.objects.create(user=request.user,title=title,image=image,content=content)
            post_con.save()
        #instance = form.save(commit=False)
        #instance.save()
            messages.success(request, 'Post has been created...')
            #return HttpResponse("Post has been created...")
    else:
        form=PostForm()
    return render(request,'post_create.html',{'form':form})    

def post_detail(request,id):
    instance = get_object_or_404(Post,id=id)

    return render(request,'post_detail.html',{'det':instance})

def post_update(request,d):
    #ins = get_object_or_404(Post,id=id)
    p=Post.objects.get(id=d)
    
    if request.method=="POST":
        
        form = PostForm(request.POST,request.FILES,instance=p)
        
        if form.is_valid():
        
            form.save()
            return HttpResponse('Updated')

    else:
        form = PostForm(instance=p)
        
    return render(request,'post_edit.html',{'form':form,'instance':p}) 

def post_del(request,id=None):
    ins = get_object_or_404(Post,id=id)
    ins.delete()
    return HttpResponse('Post has been deleted')



def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            #form.save()
            user = User.objects.create_user(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password1'],
            email = form.cleaned_data['email'])

            messages.success(request, 'You have registered successfully')
            #return HttpResponseRedirect('/accounts/register_success/')

    else:
        form = RegistrationForm()
    return render(request,'register.html',{'form':form})






