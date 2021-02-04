from django.contrib import admin
from django.urls import path, include
from administration.views import EtudiantList, EtudiantDetail,SpecialiteList,SpecialiteDetail

urlpatterns = [
    path('etudiants/', EtudiantList.as_view()),
    path('specialites/', SpecialiteList.as_view()),
    
]
