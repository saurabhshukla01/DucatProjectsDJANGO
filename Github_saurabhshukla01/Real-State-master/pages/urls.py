from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='aboutus'),
    path('search', search, name='search'),
    # path('login', views.login, name='login'),
    # path('register', views.register, name='register'),
    # path('logout', views.logout, name='logout'),
    # path('dashboard', views.dashboard, name='dashboard')
]