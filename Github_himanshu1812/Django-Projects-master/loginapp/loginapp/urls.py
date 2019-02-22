from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from mylogin.views import *
from django.conf import settings
from django.conf.urls.static import static
from search.views import search_new

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home,name='home'),
    #url(r'^login',auth_views.login,{'template_name': 'login.html'},
     #   name='login'),
    url(r'^auth-check/$',auth_view,name='check'),
    url(r'^logout',logout, name='logout'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^posts/$',index,name='post'),
    url(r'^search/$',search_new,name='search'),
    url(r'^comments/$',comments,name='comment'),
    url(r'^delete/(\d+)/$',delete,name='delete'),
    url(r'^profile/$',user_profile,name='profile'),
    url(r'^setting/password/$',password,name='password')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
