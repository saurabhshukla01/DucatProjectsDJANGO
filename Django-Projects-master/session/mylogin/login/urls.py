from django.conf.urls import patterns,include,url
from login.views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
     url(r'^$',auth_views.login),
     url(r'^logout/$',logout_page),
     
                      
     url(r'^register/$',register),
     url(r'^register/success/$',register_success),
     url(r'^accounts/profile/$',home),
   
    ]                  
