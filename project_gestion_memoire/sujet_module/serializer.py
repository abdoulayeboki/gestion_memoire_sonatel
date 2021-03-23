from rest_framework import serializers
from sujet_module.models import Sujet

class SujetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sujet
        fields = ['id', 'titre','description','etatSujet','createdDate','owner']
