"""formproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from polls.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='index'),
    path('employeeform/',login_required(EmployeeData.as_view())),
    path('register/',registration),
	path('login/',login_user),
	path('logout/',logout_user),
	path('profile/',Home.as_view()),
	path('changepass/',changepassword,name='change'),
	path('show/',login_required(EmployeeListView.as_view()),name='show'),
	path('empupdate/<int:pk>',Employeeupdate.as_view(),name='update'),
	path('empdelete/<int:pk>',Employeedelete.as_view(),name='delete'),
	path('coldelete/<int:pk>',Collegedelete.as_view(),name='deletecollege'),
	path('session/',showsession)
]