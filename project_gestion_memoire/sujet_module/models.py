from django.db import models
from enum import Enum
from django.contrib.auth.models import User

# Create your models here.

class EtatSujetEnumeration(Enum):   # A subclass of Enum
    PROPOSE= "PROPOSE"
    ACCORDE = "ACCORDE"
    VALIDE = "VALIDE"
    TERMINE = "TERMINE"
    SOUTENU = "SOUTENU"
    DEPOSE = "DEPOSE"
class Sujet(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    createdDate = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,default=None,related_name="sujets")
    etatSujet = models.CharField(max_length=10,
    choices= [(tag.value, tag.value) for tag in EtatSujetEnumeration], default="PROPOSE")
     
class Test(models.Model):
    adresse = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user = models.OneToOneField(User,on_delete=models.CASCADE)