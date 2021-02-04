
# Create your views here.
from administration.models import  Etudiant,Specialite
from administration.serializer import EtudiantSerializer, SpecialiteSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class EtudiantList(generics.ListCreateAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nom', 'prenom','promotion']
    
class EtudiantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
    
class SpecialiteList(generics.ListCreateAPIView):
    queryset = Specialite.objects.all()
    serializer_class = SpecialiteSerializer
    filter_backends = [filters.SearchFilter]
    filter_backends = [filters.OrderingFilter]
    search_fields = ['nom','code']
    ordering_fields = ['nom']
class SpecialiteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Specialite.objects.all()
    serializer_class = SpecialiteSerializer
