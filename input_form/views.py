from django.shortcuts import render

from . models import *
# Create your views here.
from django.views.generic import ListView, DetailView

class HomePageListView(ListView):
    context_object_name = 'business_list'
    queryset = BusinessType.objects.all()  
    template_name = "home.html"

class InputFormDetailView(DetailView):
    pass