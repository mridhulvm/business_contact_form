''' define path to input forms'''
from django.urls import path
from . import views

urlpatterns = [
    
    path('submit_form/', views.inputForm, name='submit_form'),

    path('', views.HomePageListView.as_view(), name='HomePageListView'),

]