from django.shortcuts import render

from .models import Sujet, SujetPostuler, SujetAccorder,SujetValider,SujetPostuler
from .serializer import (SujetSerializer,SujetAccorderSerializer,SujetPostulerSerializer,
SujetValiderSerializer)
from rest_framework import generics
from django.contrib.auth.models import User
from administration.serializer import PersonnelSerializer
from rest_framework.parsers import FileUploadParser, FormParser

from rest_framework.decorators import api_view # new
from rest_framework.response import Response # new
from rest_framework.reverse import reverse 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from coreapi.auth import TokenAuthentication
from rest_framework.exceptions import ValidationError
from  .permissions import IsOwnerOrReadOnly,IsEncadreur
from rest_framework.views import APIView
from django.http import Http404, HttpResponse
from rest_framework import status
from django.http.multipartparser import MultiPartParser



# view Sujet   
class SujetList(generics.ListCreateAPIView):
    queryset = Sujet.objects.all()
    serializer_class = SujetSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['etatSujet','personnel']
    search_fields = ['titre']
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
class SujetTermine(generics.UpdateAPIView):
    permission_classes = [IsEncadreur]
    queryset = Sujet.objects.all()
    serializer_class = SujetSerializer    

# view SujetPostuler
class SujetPostulerList(generics.ListCreateAPIView):
    queryset = SujetPostuler.objects.all()
    serializer_class = SujetPostulerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sujet','personnel']

    def perform_create(self, serializer):
        serializer.save(personnel=self.request.user.personnel)
    
    
    # def post(self, request, format=None):
    #     file_serializer = SujetPostulerSerializer(data=request.data)

    #     if file_serializer.is_valid():
    #         file_serializer.save()
    #         return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
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
    # permission_classes = []
    queryset = SujetAccorder.objects.all()
    serializer_class = SujetAccorderSerializer

# view SujetAccorder 
class SujetValiderList(generics.ListCreateAPIView):
    queryset = SujetValider.objects.all()
    serializer_class = SujetValiderSerializer

    # def perform_create(self, serializer):
    #     serializer.save(sujet.etatSujet="ACCORDE")
class SujetValiderDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = []
    queryset = SujetValider.objects.all()
    serializer_class = SujetValiderSerializer


