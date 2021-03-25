from django.contrib import admin
from django.urls import path, include
from .views import SujetList, SujetDetail,UserList,UserDetail,SujetAccordeDetail,SujetAccordeList,SujetValideDetail,SujetValideList,api_root,EnseignantPostulerList,EnseignantPostulerDetail,EtudiantPostulerList,EtudiantPostulerDetail

urlpatterns = [
    path('sujets', SujetList.as_view(), name='sujets_list'),
    path('sujets/<int:pk>', SujetDetail.as_view(), name='sujets_detail'),
    path('etudiant_postuler', EtudiantPostulerList.as_view(), name='etudiant_postuler_list'),
    path('etudiant_postuler/<int:pk>', EtudiantPostulerDetail.as_view(), name='etudiant_postuler_detail'),
    path('enseignant_postuler', EnseignantPostulerList.as_view(), name='enseignant_postuler_list'),
    path('enseignant_postuler/<int:pk>', EnseignantPostulerDetail.as_view(), name='etudiant_postuler_detail'),
    path('sujet_valide', SujetValideList.as_view(), name='sujet_valide_list'),
    path('sujet_valide/<int:pk>', SujetValideDetail.as_view(), name='sujet_valide_detail'),
    path('sujet_accorde', SujetAccordeList.as_view(), name='sujet_accorde_list'),
    path('sujet_accorde/<int:pk>', SujetAccordeDetail.as_view(), name='sujet_accorde_detail'),
    path('users/', UserList.as_view()), # new
    path('users/<int:pk>/', UserDetail.as_view()), 
    path('', api_root),
]
