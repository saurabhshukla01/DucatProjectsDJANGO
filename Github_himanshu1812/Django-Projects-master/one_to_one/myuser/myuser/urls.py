
from django.conf.urls import url
from django.contrib import admin
from myuserapp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index),
    url(r'^form/$',user_form)
]
