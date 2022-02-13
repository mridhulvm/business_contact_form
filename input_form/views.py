from django.shortcuts import render
from django.http import JsonResponse

from .models import *

import logging
logger = logging.getLogger(__name__)
# Create your views here.

from django.views.generic import ListView, DetailView

class HomePageListView(ListView):
    ''' render home page'''
    context_object_name = 'business_list'
    queryset = BusinessType.objects.all()  
    template_name = "home.html"

def inputForm(request):
    ''' record input form submission through ajax '''
    if request.method == "POST" :
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        business = request.POST.get('business')
        phone_number = request.POST.get('phone_number')
        logger.warning(name, contact, business, phone_number)
        InputForm.objects.create(
        name = name, 
        contact = contact, 
        business_type_id = business, 
        phone_number = phone_number
        )
        data = {'status':True,'message':'Form submitted successfully'}
        return JsonResponse(data)
        
    data = {'status':False,'message':'Form submittion error'}
    return JsonResponse(data)

