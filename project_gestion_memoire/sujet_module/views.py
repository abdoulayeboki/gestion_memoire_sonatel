from django.shortcuts import render

from sujet_module.models import Sujet
from sujet_module.serializer import SujetSerializer
from rest_framework import generics

# view Sujet   
class SujetList(generics.ListCreateAPIView):
    queryset = Sujet.objects.all()
    serializer_class = SujetSerializer

    
class SujetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sujet.objects.all()
    serializer_class = SujetSerializer