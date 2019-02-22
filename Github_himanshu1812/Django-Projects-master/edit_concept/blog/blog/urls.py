"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from vblog.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index),
    url(r'^post_login/$',login),
    url(r'^accounts/auth/$',auth_view),
    url(r'^search_query/$',search),
    url(r'^logout/$',logout_page),
    #url(r'^accounts/loggedin/$',loggedin),
    url(r'^post_detail/(?P<id>\d+)/$',post_detail,name='detail'),
    url(r'^accounts/register/$',register_user),
    url(r'^postcreate/$',post_create),
    url(r'^postupdate/edit/(\d+)/$',post_update,name='update'),
    url(r'^postdelete/(?P<id>\d+)/$',post_del,name='delete'),
    
]   + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)






