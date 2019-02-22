from django.urls import path
from .views import registration, UserCreateAPIView

urlpatterns = [
    path('register/',registration,name='registration'),
    path('api/register/',UserCreateAPIView.as_view(),name='apiregister')
]