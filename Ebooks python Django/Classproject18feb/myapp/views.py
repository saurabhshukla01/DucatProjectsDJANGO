from django.shortcuts import render
from django.views.generic import TemplateView

class Sample(TemplateView):
    template_name = "myapp/home.html"

