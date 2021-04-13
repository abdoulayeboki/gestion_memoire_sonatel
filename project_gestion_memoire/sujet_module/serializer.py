from rest_framework import serializers
from .models import Sujet,SujetPostuler,SujetAccorder,SujetValider
from django.contrib.auth.models import User
from administration.serializer import PersonnelSerializer
from administration.models import Personnel
from rest_framework.fields import SerializerMethodField
from rest_framework.validators import UniqueTogetherValidator
class SujetSerializer(serializers.ModelSerializer):
    personnel = PersonnelSerializer(read_only=True)
    personnelPostuler = PersonnelSerializer(many=True,read_only=True)
    personnelAccorder = PersonnelSerializer(many=True,read_only=True)
    personnelValider = PersonnelSerializer(many=True,read_only=True)
    class Meta:
        model = Sujet
        # fields = '__all__'
        fields = ('id','titre','description','etatSujet','createdDate','createdDate','personnel','personnelPostuler','personnelAccorder','personnelValider')


class SujetPostulerSerializer(serializers.ModelSerializer):
    personnel = PersonnelSerializer(read_only=True)
    class Meta:
        model = SujetPostuler
        fields = ('motivation','cv','sujet','personnel') 


class SujetAccorderSerializer(serializers.ModelSerializer):

    class Meta:
        model = SujetAccorder
        fields = '__all__' #('id','sujet','personnel','valide','sujets','personnels') 
class SujetValiderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SujetValider
        fields = '__all__'
   