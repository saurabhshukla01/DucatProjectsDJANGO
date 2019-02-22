

from django.conf.urls import url
from django.contrib import admin
from myapp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index),
    url(r'^detail/(\d+)/(\w+)/$',detail,name='detail'),
    url(r'^delete/(\d+)/$',delete_record,name='det'),
    url(r'^contact/$',contact),
    url(r'^success/$',success),


    
    
]
