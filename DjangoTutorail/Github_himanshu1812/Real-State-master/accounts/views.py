from .froms import RegisterForm, LoginForm
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile
from django.contrib import messages
from django.views.generic import CreateView,UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        email = request.POST['email']
        if Profile.objects.filter(email=email).exists():
            messages.error(request, 'email already exists')
            return redirect('register')
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'user register succesfully')
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request,'accounts/register.html', {'form':form})

def user_logout(request):
        logout(request)
        messages.success(request, 'user logout succesfully')
        return redirect('/')


def user_login(request):
    login_form=LoginForm(request.POST or None)
    messages.success(request, 'user logout succesfully')
    context = {
        "form": login_form
    }
    if login_form.is_valid():
        username=login_form.cleaned_data.get("username")
        password=login_form.cleaned_data.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            print('error')
    return render(request,'accounts/login.html',context)


class Dashboard(DetailView):
    template_name = 'accounts/dashboard.html'
    queryset = Profile.objects.all()

    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(Dashboard, self).dispatch(request, *args, **kwargs)


# class ProfileUpdate(UpdateView, SuccessMessageMixin):
#     success_message = 'Update sucessfully'
#     model = Profile
#     fields = '__all__'






