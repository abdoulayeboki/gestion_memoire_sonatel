from rest_framework import serializers
from .models import Encadrement,Evenement,Ressource
# from administration.models import Personnel PersonnelSerializer
from administration.serializer import PersonnelSerializer
class EncadrementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encadrement
        # fields = '__all__'
        fields = ('id','sujet')

class EvenementSerializer(serializers.ModelSerializer):
    owner = PersonnelSerializer(read_only=True)
    class Meta:
        model = Evenement
        # fields = '__all__'
        fields = ('titre','duree','description','dateEvenement','encadrement','owner')
class RessourceSerializer(serializers.ModelSerializer):
    owner = PersonnelSerializer(read_only=True)
    class Meta:
        model = Ressource
        # fields = '__all__'
        fields = ('titre','date','file','encadrement','owner')
