from django.contrib import admin
from django.urls import path, include
from sujet_module.views import SujetList, SujetDetail


urlpatterns = [
    path('sujets', SujetList.as_view(), name='sujets_list'),
    path('sujets/<int:pk>', SujetDetail.as_view(), name='sujets_detail')

    
]
