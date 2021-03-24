from django.contrib import admin
from django.urls import path, include
from .views import SujetList, SujetDetail,UserList,UserDetail,api_root,EtudiantPostulerList,EtudiantPostulerDetail


urlpatterns = [
    path('sujets', SujetList.as_view(), name='sujets_list'),
    path('sujets/<int:pk>', SujetDetail.as_view(), name='sujets_detail'),
    path('etudiant_postuler', EtudiantPostulerList.as_view(), name='etudiant_postuler_list'),
    path('etudiant_postuler/<int:pk>', EtudiantPostulerDetail.as_view(), name='etudiant_postuler_detail'),
    path('users/', UserList.as_view()), # new
    path('users/<int:pk>/', UserDetail.as_view()), 
    path('', api_root),
]
