from django.shortcuts import render

from .models import Sujet, EtudiantPostuler
from .serializer import SujetSerializer, UserSerializer, EtudiantPostulerSerializer
from rest_framework import generics
from django.contrib.auth.models import User

from rest_framework.decorators import api_view # new
from rest_framework.response import Response # new
from rest_framework.reverse import reverse # new
# view Sujet   
class SujetList(generics.ListCreateAPIView):
    # queryset = Sujet.objects.all()
    serializer_class = SujetSerializer
    def perform_create(self, serializer): # new
        serializer.save(owner=self.request.user)
    def get_queryset(self):
        user = self.request.user
        # return Sujet.objects.with_counts()
        return Sujet.objects.filter(owner=user)

    
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





class UserList(generics.ListAPIView): # new
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView): # new
    queryset = User.objects.all()
    serializer_class = UserSerializer
@api_view(['GET']) # new
def api_root(request, format=None):
    return Response({
        'sujet': reverse('sujets_list', request=request, format=format),
    })