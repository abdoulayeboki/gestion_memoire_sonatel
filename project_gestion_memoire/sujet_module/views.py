from django.shortcuts import render

from .models import Sujet, EtudiantPostuler,EnseignantPostuler,SujetValide, SujetAccorde
from .serializer import SujetSerializer, UserSerializer,SujetAccordeSerializer, SujetValideSerializer,EtudiantPostulerSerializer,EnseignantPostulerSerializer
from rest_framework import generics
from django.contrib.auth.models import User

from rest_framework.decorators import api_view # new
from rest_framework.response import Response # new
from rest_framework.reverse import reverse 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from coreapi.auth import TokenAuthentication

# view Sujet   
class SujetList(generics.ListCreateAPIView):
    queryset = Sujet.objects.all()
    serializer_class = SujetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['etatSujet','owner']
    # def get_queryset(self):
    #     user = self.request.user
    #     return Sujet.objects.filter(owner=user)

    
class SujetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sujet.objects.all()
    serializer_class = SujetSerializer

# view EtudiantPostuler   
class EtudiantPostulerList(generics.ListCreateAPIView):
    queryset = EtudiantPostuler.objects.all()
    serializer_class = EtudiantPostulerSerializer
    
class EtudiantPostulerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EtudiantPostuler.objects.all()
    serializer_class = EtudiantPostulerSerializer

# view EnseignentPostuler   
class EnseignantPostulerList(generics.ListCreateAPIView):
    queryset = EnseignantPostuler.objects.all()
    serializer_class = EnseignantPostulerSerializer
class EnseignantPostulerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EnseignantPostuler.objects.all()
    serializer_class = EnseignantPostulerSerializer
    
# view SujetValide   
class SujetValideList(generics.ListCreateAPIView):
    queryset = SujetValide.objects.all()
    serializer_class = SujetValideSerializer
class SujetValideDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SujetValide.objects.all()
    serializer_class = SujetValideSerializer

# view SujetAccorde 
class SujetAccordeList(generics.ListCreateAPIView):
    queryset = SujetAccorde.objects.all()
    serializer_class = SujetAccordeSerializer
class SujetAccordeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SujetAccorde.objects.all()
    serializer_class = SujetAccordeSerializer


class UserList(generics.ListAPIView): # new
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView): # new
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
# l'url par defaut
@api_view(['GET']) # new
def api_root(request, format=None):
    return Response({
        'sujet': reverse('sujets_list', request=request, format=format),
    })