
from django.conf.urls import url
from django.contrib import admin
from basic.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index),
    url(r'^pub_form/$',Pub_form),
    url(r'^book_form/$',book_form),
    
]
