from django.shortcuts import render, HttpResponse
from .forms import UserForm
from .models import User
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import UserCreateSerializer

def registration(request):
    if request.method == 'POST':
        form=UserForm(request.POST)
        if form.is_valid():
            house_name = form.cleaned_data['house_name']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(house_name=house_name,
			name=name,email=email,password=password)
            return HttpResponse('<h1>Happy Birthday.!!!!!!!!!</h1>')       
    else:
        form = UserForm()
    return render(request,'registration.html',{'form':form})        

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

