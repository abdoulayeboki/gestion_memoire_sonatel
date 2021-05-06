from django.shortcuts import render
from .models import Encadrement,Evenement,Ressource
from .serializer import EncadrementSerializer,EvenementSerializer,RessourceSerializer,EncadrementSerializerList
from .permissions import  IntegrityPermission

from rest_framework import generics
# Create your views here.
class EncadrementCreate(generics.CreateAPIView):
    queryset = Encadrement.objects.all()
    serializer_class = EncadrementSerializer
class EncadrementList(generics.ListAPIView):
    queryset = Encadrement.objects.all()
    serializer_class = EncadrementSerializerList

class EncadrementDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IntegrityPermission]
    queryset = Encadrement.objects.all()
    serializer_class = EvenementSerializer


class EvenementList(generics.ListCreateAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.personnel)


class EvenementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer

class RessourceList(generics.ListCreateAPIView):
    queryset = Ressource.objects.all()
    serializer_class = RessourceSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.personnel)


class RessourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ressource.objects.all()
    serializer_class = RessourceSerializer