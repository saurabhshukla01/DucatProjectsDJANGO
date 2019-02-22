from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .seriallizers import ProfileSerializers

class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers
# Create your views here.
