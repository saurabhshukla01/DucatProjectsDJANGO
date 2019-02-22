from django.shortcuts import render, HttpResponse
from .forms import UserForm
from .models import User, Room
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import UserCreateSerializer, RoomCreateSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
        

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class RoomCreateAPIView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    serializer_class = RoomCreateSerializer

    def get(self, request, format=None):
        print(request.user)
        room = Room.objects.filter(user=request.user)
        serializer = RoomCreateSerializer(room, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        room = RoomCreateSerializer(data=request.data)
        if room.is_valid():
            room.save()
            return Response(room.data, status=status.HTTP_201_CREATED)
        return Response(room.errors, status=status.HTTP_400_BAD_REQUEST)