from rest_framework import serializers
from sujet_module.models import Sujet, EnseignantPostuler,EtudiantPostuler,SujetValide,SujetAccorde
from django.contrib.auth.models import User
from administration.models import Etudiant
class SujetSerializer(serializers.ModelSerializer):
    # postulants = serializers.HyperlinkedRelatedField(many=True, read_only=True,view_name='etudiants_detail')
    class Meta:
        model = Sujet
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    sujets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Sujet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'sujets')
class EtudiantPostulerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EtudiantPostuler
        fields = '__all__' 

class EnseignantPostulerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnseignantPostuler
        fields = '__all__' 
class SujetValideSerializer(serializers.ModelSerializer):
    class Meta:
        model = SujetValide
        fields = '__all__' 
class SujetAccordeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SujetAccorde
        fields = '__all__' 