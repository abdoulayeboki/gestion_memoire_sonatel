from rest_framework import serializers
from .models import Encadrement,Evenement,Ressource
# from administration.models import Personnel

class EncadrementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encadrement
        # fields = '__all__'
        fields = ('id','sujet')

class EvenementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evenement
        fields = '__all__'
class RessourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ressource
        fields = '__all__'
