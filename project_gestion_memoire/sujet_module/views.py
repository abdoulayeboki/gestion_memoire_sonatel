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

# view Sujet   
class SujetList(generics.ListCreateAPIView):
    queryset = Sujet.objects.all()
    serializer_class = SujetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['etatSujet','personnel']
    # def get_queryset(self):
    #     user = self.request.user
    #     return Sujet.objects.filter(owner=user)

    
class SujetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sujet.objects.all()
    serializer_class = SujetSerializer

# view SujetPostuler   
class SujetPostulerList(generics.ListCreateAPIView):
    queryset = SujetPostuler.objects.all()
    serializer_class = SujetPostulerSerializer
    
class SujetPostulerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SujetPostuler.objects.all()
    serializer_class = SujetPostulerSerializer

# view SujetAccorder 
class SujetAccorderList(generics.ListCreateAPIView):
    queryset = SujetAccorder.objects.all()
    serializer_class = SujetAccorderSerializer
class SujetAccorderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SujetAccorder.objects.all()
    serializer_class = SujetAccorderSerializer


