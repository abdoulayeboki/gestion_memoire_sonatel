from django.contrib import admin
from django.urls import path, include
from .views import ( EncadrementList,EncadrementDetail,RessourceList,RessourceDetail, EvenementList,EvenementDetail)

urlpatterns = [
    path('', EncadrementList.as_view(), name='encadrements_list'),
    path('<int:pk>/', EncadrementDetail.as_view(), name='encadrements_detail'),
    path('ressources', RessourceList.as_view(), name='ressources_list'),
    path('ressources/<int:pk>/', RessourceDetail.as_view(), name='ressources_detail'),
    path('evenements', EvenementList.as_view(), name='evenements_list'),
    path('evenements/<int:pk>/', EvenementDetail.as_view(), name='evenements_detail'),
]
