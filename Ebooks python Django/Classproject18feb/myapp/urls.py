from django.urls import path
from django.views.generic import TemplateView
from .views import Sample


urlpatterns = [
    path('',TemplateView.as_view(template_name="myapp/index.html"),name="index"),
    path('home/',Sample.as_view(),name="home")


]