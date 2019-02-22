from django.urls import path
from .views import listings,listing, SaveProperty
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('listings/', listings, name='listings'),
    path('listing/<int:id>/', listing, name='property'),
    path('postproperty/', login_required(SaveProperty.as_view()) , name='postproperty'),
]