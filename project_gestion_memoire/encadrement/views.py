from django.shortcuts import render
from .models import Encadrement,Evenement,Ressource
from .serializer import EncadrementSerializer,EvenementSerializer,RessourceSerializer
from .permissions import  IntegrityPermission
# from requests.models import Response
# from rest_framework.reverse import reverse
from rest_framework import generics
# Create your views here.
class EncadrementList(generics.ListCreateAPIView):
    # permission_classes = [IntegrityPermission]
    queryset = Encadrement.objects.all()
    serializer_class = EncadrementSerializer


class EncadrementDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IntegrityPermission]
    queryset = Encadrement.objects.all()
    serializer_class = EncadrementSerializer

class EvenementList(generics.ListCreateAPIView):
    # permission_classes = [IntegrityPermission]
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer


class EvenementDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IntegrityPermission]
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer

class RessourceList(generics.ListCreateAPIView):
    # permission_classes = [IntegrityPermission]
    queryset = Ressource.objects.all()
    serializer_class = RessourceSerializer


class RessourceDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IntegrityPermission]
    queryset = Ressource.objects.all()
    serializer_class = RessourceSerializer