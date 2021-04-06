from rest_framework import serializers
from administration.models import Classe, Departement, Enseignent, Etudiant, Filiere, Personnel, Promotion, Specialite
from django.contrib.auth.models import User
# from sujet_module.serializer import SujetAccorderSerializer, SujetSerializer
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
    promotion =  PromotionSerializer()
    # sujetsPostuler = SujetSerializer(read_only=True,many=True)
    # sujetsAccorder = SujetAccorderSerializer(read_only=True,many=True)
    classe = ClasseSerializer()
    class Meta:
        model = Etudiant
        fields = ['id', 'nom', 'prenom','telephon','email', 'ine','promotion','classe']

class EnseignentSerializer(serializers.ModelSerializer):
    departement =  DepartementSerializer(read_only=True)
    # sujetsPostuler = SujetSerializer(read_only=True,many=True)
    # sujetsAccorder = SujetAccorderSerializer(read_only=True,many=True)
    class Meta:
        model = Enseignent
        fields = '__all__'

class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        # fields = ['id', 'profil','user']
        fields ='__all__'

