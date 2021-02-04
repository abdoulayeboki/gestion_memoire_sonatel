from rest_framework import serializers
from administration.models import Etudiant, Promotion, Specialite, Classe, Filiere,Enseignent,Departement
from django.contrib.auth.models import User

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['id', 'code', 'nom']
class FiliereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filiere
        fields = ['code', 'nom']
class SpecialiteSerializer(serializers.ModelSerializer):
    filiere = FiliereSerializer()
    class Meta:
        model = Specialite
        fields = ['id', 'code', 'nom','filiere','niveau']
class ClasseSerializer(serializers.ModelSerializer):
    specialite = SpecialiteSerializer()
    class Meta:
        model = Classe
        fields = ['id', 'code', 'specialite','anneeScolaire']
class EtudiantSerializer(serializers.ModelSerializer):
    promotion =  PromotionSerializer(read_only=True)
    classe = ClasseSerializer()
    class Meta:
        model = Etudiant
        fields = ['id', 'nom', 'prenom', 'ine','promotion','classe']
class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = ['id', 'nom','code']
class EnseignentSerializer(serializers.ModelSerializer):
    departement =  DepartementSerializer(read_only=True)
    class Meta:
        model = Enseignent
        fields = ['id', 'nom', 'prenom', 'cni','departement']
