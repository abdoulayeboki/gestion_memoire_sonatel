from django.contrib.gis import serializers
from sujet_module.models import Sujet
from django.contrib.auth.models import User
from administration.models import Personnel
from administration.serializer import PersonnelSerializer
from rest_framework import serializers
from sujet_module.serializer import SujetSerializer
from rest_framework.relations import PrimaryKeyRelatedField

class UserSerializer(serializers.ModelSerializer):
    sujets = SujetSerializer(many=True,read_only=True)
    # personnel = PrimaryKeyRelatedField(queryset=Personnel.objects.all())
    personnel = PersonnelSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username','password','email', 'sujets','personnel')

        extra_kwargs = {"password":{"write_only":True}}
    
    # def create(self, validated_data):
    #     username = validated_data["username"]
    #     password = validated_data["password"]
    #     email = validated_data["email"]
    #     user_obj = User(
    #         username =username,
    #         email = email
    #     )
    #     user_obj.set_password(password)
    #     user_obj.save()
    #     return validated_data
    #     # return super().create(validated_data)