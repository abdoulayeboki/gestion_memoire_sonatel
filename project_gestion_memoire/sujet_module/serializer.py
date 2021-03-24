from rest_framework import serializers
from sujet_module.models import Sujet
from django.contrib.auth.models import User
from sujet_module.models import EtudiantPostuler
# from administration.serializer import EtudiantSerializer
class SujetSerializer(serializers.ModelSerializer):
    postulants = serializers.HyperlinkedRelatedField(many=True, read_only=True,view_name='etudiants_detail')

    class Meta:
        model = Sujet
        fields = ['id', 'titre','description','etatSujet','createdDate','owner','postulants']
class UserSerializer(serializers.ModelSerializer):
    sujets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Sujet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'sujets')
class EtudiantPostulerSerializer(serializers.ModelSerializer):
    # etudiant = serializers.HyperlinkedRelatedField( read_only=True,view_name='etudiants_detail')
    # sujet = serializers.HyperlinkedRelatedField( read_only=True,view_name='sujets_detail')
    etudiant = serializers.IntegerField(source="etudiant.id",read_only=True)
    sujet = serializers.IntegerField(source="sujet.id",read_only=True)
    class Meta:
        model = EtudiantPostuler
        fields = '__all__' 