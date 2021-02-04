from rest_framework import serializers
from administration.models import Etudiant, Promotion, Specialite, Classe, Filiere
from django.contrib.auth.models import User

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['id', 'code', 'nom']
class EtudiantSerializer(serializers.ModelSerializer):
    promotion =  PromotionSerializer(read_only=True)
    class Meta:
        model = Etudiant
        fields = ['id', 'nom', 'prenom', 'ine','promotion']

class SpecialiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialite
        fields = ['id', 'code', 'nom']
