from django.contrib import admin
from django.urls import path, include
from administration.views import PersonnelList,PersonnelDetail,EtudiantList,PromotionList, EtudiantDetail,SpecialiteList,DepartementList,PromotionDetail,DepartementDetail,SpecialiteDetail,EnseignentDetail,ClasseList,EnseignentList, ClasseDetail,FiliereList,FiliereDetail


urlpatterns = [
    path('etudiants', EtudiantList.as_view(), name='etudiants_list'),
    path('etudiants/<int:pk>', EtudiantDetail.as_view(), name='etudiants_detail'),
    path('specialites', SpecialiteList.as_view(), name='specialites_list'),
    path('specialites/<int:pk>', SpecialiteDetail.as_view(), name='specialites_detail'),
    path('classes', ClasseList.as_view(), name='classes_list'),
    path('classes/<int:pk>', ClasseDetail.as_view(), name='classes_detail'),
    path('filieres', FiliereList.as_view(), name='filieres_list'),
    path('filieres/<int:pk>', FiliereDetail.as_view(), name='filieres_detail'),
    path('enseignents', EnseignentList.as_view(), name='enseignents_list'),
    path('enseignents/<int:pk>', EnseignentDetail.as_view(), name='enseignents_detail'),
    path('departements', DepartementList.as_view(), name="departements_list"),
    path('departements/<int:pk>', DepartementDetail.as_view(), name="departements_detail"),
    path('promotions', PromotionList.as_view(), name="promotions_list"),
    path('promotions/<int:pk>', PromotionDetail.as_view(), name="promotions_detail"),

    path('personnels/', PersonnelList.as_view(), name="personnel_list"),
    path('personnels/<int:pk>', PersonnelDetail.as_view(), name="personnel_detail"),

    
]
