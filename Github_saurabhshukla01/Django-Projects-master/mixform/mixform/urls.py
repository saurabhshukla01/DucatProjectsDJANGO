
from django.conf.urls import url
from django.contrib import admin
from myform.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index),
    url(r'^home/$',home,name='home')
]
