''' define path to input forms'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageListView.as_view(), name='HomePageListView'),
    path('input_form/', views.InputFormDetailView.as_view(), name='InputFormDetailView'),

]