from django.contrib import admin
from django.urls import path, include
from .views import SujetList, SujetDetail,UserList,UserDetail,SujetAccorderDetail,SujetAccorderList,api_root,SujetPostulerList,SujetPostulerDetail

urlpatterns = [
    path('sujets', SujetList.as_view(), name='sujets_list'),
    path('sujets/<int:pk>/', SujetDetail.as_view(), name='sujets_detail'),
    path('sujet_postuler', SujetPostulerList.as_view(), name='etudiant_postuler_list'),
    path('sujet_postuler/<int:pk>/', SujetPostulerDetail.as_view(), name='etudiant_postuler_detail'),
    path('sujet_accorde/', SujetAccorderList.as_view(), name='sujet_accorde_list'),
    path('sujet_accorde/<int:pk>/', SujetAccorderDetail.as_view(), name='sujet_accorde_detail'),
    path('users/', UserList.as_view()), # new
    path('users/<int:pk>/', UserDetail.as_view()), 
    path('', api_root),
]
