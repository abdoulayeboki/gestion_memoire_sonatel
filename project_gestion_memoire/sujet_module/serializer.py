from rest_framework import serializers
from sujet_module.models import Sujet,SujetPostuler,SujetAccorder
from django.contrib.auth.models import User
from administration.serializer import PersonnelSerializer
class SujetSerializer(serializers.ModelSerializer):
    personnel = PersonnelSerializer(read_only=True)
    personnelPostuler = PersonnelSerializer(many=True,read_only=True)
    personnelAccorder = PersonnelSerializer(many=True,read_only=True)
    class Meta:
        model = Sujet
        # fields = '__all__'
        fields = ('id','titre','description','etatSujet','createdDate','createdDate','personnel','personnelPostuler','personnelAccorder')

class SujetPostulerSerializer(serializers.ModelSerializer):
    personnel = PersonnelSerializer(read_only=True)
    class Meta:
        model = SujetPostuler
        fields = ('motivation','cv','sujet','personnel') 


class SujetAccorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SujetAccorder
        fields = '__all__' 