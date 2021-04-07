from django.shortcuts import render

from .models import Sujet, SujetPostuler, SujetAccorder
from .serializer import SujetSerializer,SujetAccorderSerializer,SujetPostulerSerializer
from rest_framework import generics
from django.contrib.auth.models import User

from rest_framework.decorators import api_view # new
from rest_framework.response import Response # new
from rest_framework.reverse import reverse 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from coreapi.auth import TokenAuthentication
from rest_framework.exceptions import ValidationError
from  .permissions import IsOwnerOrReadOnly,IsOwnerOrReadOnlyAccorde

# view Sujet   
class SujetList(generics.ListCreateAPIView):
    queryset = Sujet.objects.all()
    serializer_class = SujetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['etatSujet','personnel']
    # def get_queryset(self):
    #     user = self.request.user
    #     return Sujet.objects.filter(owner=user)
    def perform_create(self, serializer):
        serializer.save(personnel=self.request.user.personnel)
    
class SujetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Sujet.objects.all()
    serializer_class = SujetSerializer
    
    # def  get_queryset(self):
    #     return Sujet.objects.filter(personnel=self.request.user.personnel)
    

# view SujetPostuler   
class SujetPostulerList(generics.ListCreateAPIView):
    queryset = SujetPostuler.objects.all()
    serializer_class = SujetPostulerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sujet','personnel']

    def perform_create(self, serializer):
        serializer.save(personnel=self.request.user.personnel)
    
class SujetPostulerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SujetPostuler.objects.all()
    serializer_class = SujetPostulerSerializer

# view SujetAccorder 
class SujetAccorderList(generics.ListCreateAPIView):
    queryset = SujetAccorder.objects.all()
    serializer_class = SujetAccorderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sujet','personnel']

    # def perform_create(self, serializer):
    #     serializer.save(sujet.etatSujet="ACCORDE")
class SujetAccorderDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnlyAccorde]
    queryset = SujetAccorder.objects.all()
    serializer_class = SujetAccorderSerializer


