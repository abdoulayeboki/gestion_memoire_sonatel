from django.contrib import admin
from django.urls import path, include
from administration.views import EtudiantList, EtudiantDetail,SpecialiteList,SpecialiteDetail,EnseignentDetail,ClasseList,EnseignentList, ClasseDetail,FiliereList,FiliereDetail

urlpatterns = [
    path('etudiants/', EtudiantList.as_view()),
    path('etudiants/<int:pk>/', EtudiantDetail.as_view()),
    path('specialites/', SpecialiteList.as_view()),
    path('specialites/<int:pk>/', SpecialiteDetail.as_view()),
    path('classes/', ClasseList.as_view()),
    path('classes/<int:pk>/', ClasseDetail.as_view()),
    path('filieres/', FiliereList.as_view()),
    path('filieres/<int:pk>/', FiliereDetail.as_view()),
    path('enseignents/', EnseignentList.as_view()),
    path('enseignents/<int:pk>/', EnseignentDetail.as_view()),
    
]
