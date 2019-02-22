
from django.conf.urls import url
from django.contrib import admin
from newapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home),
    #url(r'^auth-check/$',auth_view,name='check'),
    url(r'^invalid/$',invalid_login),
    url(r'^logout/$',logout),
    url(r'^signup/$', signup, name='signup'),
    url(r'^detail/(\d+)/$',detail, name='detail'),
    url(r'^edit/(\d+)/$',edit, name='edit'),
    url(r'^delete/(\d+)/$',delete, name='delete'),
    url(r'^share/(\d+)/$',share_post, name='share'),
    url(r'^share_post/(\d+)/(\d+)/$',sharepost,name='post_share'),
]+ static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)








