"""University URL Configuration

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
from onlineportal.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',AppForm,name='register'),
    path('admin/', admin.site.urls),
    path('home/',homepage,name='register1'),
    path('index/',index_proffdetail,name='register2'),
    path('index1/',index_proffdetaillist,name='register3'),
    path('login/',loginuser,name="login"),
    path('logout/',logoutuser,name="logout"),
    path('university/',addUniversity,name="university"),
    path('proff/',addproff_of_university,name="proff"),
    path('proffdetail/',showproff_details,name="proff_details"),
    path('universitydetail/<int:id>',Universitydetail,name="universodetail"),
    path('proffdetail/<int:id>',proff_details1,name="proffodetail"),
    path('proffdetaillist/<int:id>',proff_detaillist,name="proffodetaillist")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


