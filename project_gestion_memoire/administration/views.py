
# Create your views here.
from administration.models import (Etudiant,Personnel,Specialite, Classe,
Filiere,Enseignent,Departement, Promotion)  
from administration.serializer import (EtudiantSerializer,PersonnelSerializer, SpecialiteSerializer,
DepartementSerializer,PromotionSerializer, 
ClasseSerializer,FiliereSerializer,EnseignentSerializer) 
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class EtudiantList(generics.ListCreateAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['promotion','classe','classe__specialite','classe__specialite__filiere','classe__specialite__niveau']
    search_fields = ['nom','prenom','ine']
    
class EtudiantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
    
class SpecialiteList(generics.ListCreateAPIView):
    queryset = Specialite.objects.all()
    serializer_class = SpecialiteSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['filiere','niveau']
    search_fields = ['nom','code']
class SpecialiteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Specialite.objects.all()
    serializer_class = SpecialiteSerializer
# view Classe   
class ClasseList(generics.ListCreateAPIView):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['specialite','specialite__filiere']
    search_fields = ['code','anneeScolaire']
    
class ClasseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Classe.objects.all()
    serializer_class = FiliereSerializer


# view Filiere   
class FiliereList(generics.ListCreateAPIView):
    queryset = Filiere.objects.all()
    serializer_class = FiliereSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['departement']
    search_fields = ['nom','code']
    
class FiliereDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filiere.objects.all()
    serializer_class = FiliereSerializer

# view Enseignent   
class EnseignentList(generics.ListCreateAPIView):
    queryset = Enseignent.objects.all()
    serializer_class = EnseignentSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['departement']
    search_fields = ['nom','prenom','cni']
    
class EnseignentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enseignent.objects.all()
    serializer_class = EnseignentSerializer

# view Departement   
class DepartementList(generics.ListCreateAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nom','code']
    
class DepartementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer

# view Promotion   
class PromotionList(generics.ListCreateAPIView):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    
    
class PromotionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

class PersonnelList(generics.ListCreateAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']
    
class PersonnelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer