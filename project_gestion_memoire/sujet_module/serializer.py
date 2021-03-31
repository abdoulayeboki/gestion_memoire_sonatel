from rest_framework import serializers
from sujet_module.models import Sujet,SujetPostuler,SujetAccorder
from django.contrib.auth.models import User
from administration.models import Etudiant
class SujetSerializer(serializers.ModelSerializer):
    # postulants = serializers.HyperlinkedRelatedField(many=True, read_only=True,view_name='etudiants_detail')
    class Meta:
        model = Sujet
        fields = '__all__'

class SujetPostulerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SujetPostuler
        fields = '__all__' 


class SujetAccorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SujetAccorder
        fields = '__all__' 