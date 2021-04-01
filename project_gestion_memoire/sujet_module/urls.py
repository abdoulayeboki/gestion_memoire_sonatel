from django.contrib import admin
from django.urls import path, include
from .views import SujetList, SujetDetail,SujetAccorderDetail,SujetAccorderList,SujetPostulerList,SujetPostulerDetail

urlpatterns = [
    path('sujets', SujetList.as_view(), name='sujets_list'),
    path('sujets/<int:pk>/', SujetDetail.as_view(), name='sujets_detail'),
    path('sujet_postuler', SujetPostulerList.as_view(), name='sujet_postuler_list'),
    path('sujet_postuler/<int:pk>/', SujetPostulerDetail.as_view(), name='sujet__postuler_detail'),
    path('sujet_accorde/', SujetAccorderList.as_view(), name='sujet_accorde_list'),
    path('sujet_accorde/<int:pk>/', SujetAccorderDetail.as_view(), name='sujet_accorde_detail'),
    
]
