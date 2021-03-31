from django.contrib.gis import serializers
from sujet_module.models import Sujet
from django.contrib.auth.models import User
from administration.models import Personnel
from administration.serializer import PersonnelSerializer
from rest_framework import serializers
from sujet_module.serializer import SujetSerializer

class UserSerializer(serializers.ModelSerializer):
    sujets = SujetSerializer(many=True,read_only=True)
    personnel = PersonnelSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'sujets','personnel','password')