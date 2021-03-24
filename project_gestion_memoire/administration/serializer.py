from rest_framework import serializers
from administration.models import Etudiant, Promotion, Specialite, Classe, Filiere,Enseignent,Departement
from django.contrib.auth.models import User
# from sujet_module.serializer import SujetSerializer
# from sujet_module.serializer import EtudiantPostulerSerializer

class DepartementSerializer(serializers.HyperlinkedModelSerializer):
    # departement = serializers.HyperlinkedIdentityField(view_name='departements_detail', format='html')
    class Meta:
        model = Departement
        fields = ['id', 'nom','code']
class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['id', 'code', 'nom']
class FiliereSerializer(serializers.ModelSerializer):
    departement =  DepartementSerializer(read_only=True)
    class Meta:
        model = Filiere
        fields = ['id','code', 'nom','departement']
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
    sujetsPostuler = serializers.HyperlinkedRelatedField(many=True, read_only=True,view_name='sujets_detail')
    classe = ClasseSerializer()
    class Meta:
        model = Etudiant
        fields = ['id', 'nom', 'prenom','telephon','email', 'ine','promotion','classe','sujetsPostuler']

class EnseignentSerializer(serializers.ModelSerializer):
    departement =  DepartementSerializer(read_only=True)
    sujetsPostuler = serializers.HyperlinkedRelatedField(many=True, read_only=True,view_name='sujets_detail')
    # sujetsPostuler = serializers.IntegerField(source ="sujet.id", read_only=True)
    class Meta:
        model = Enseignent
        fields = '__all__'
