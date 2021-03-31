from django.db import models
from enum import Enum
from django.contrib.auth.models import User
from django.db.models.functions import Coalesce
from administration.models import Enseignent, Etudiant, Personnel
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
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="sujets")
    etatSujet = models.CharField(max_length=10,
    choices= [(tag.value, tag.value) for tag in EtatSujetEnumeration], default="PROPOSE")
    
    def __str__(self):
        return self.titre
    
    # def save(self,force_update=True, *args, **kwargs):
    #     self.etatSujet = "VALIDE"
    #     super().save(*args, **kwargs)  

class SujetPostuler(models.Model):
    datePostuler = models.DateTimeField(auto_now_add=True)
    motivation = models.TextField()
    cv = models.CharField(max_length=255)
    personnel = models.ForeignKey(Personnel,on_delete=models.CASCADE,related_name="sujetsPostule")
    sujet = models.ForeignKey(Sujet,on_delete=models.CASCADE,related_name="personnesPostulant")

    class Meta:
        unique_together =['personnel','sujet']
    def __str__(self):
        return  self.cv

class SujetAccorder(models.Model):
    dateAccorde = models.DateTimeField(auto_now_add=True)
    valide = models.BooleanField(default=False)
    sujetPostuler = models.ForeignKey(SujetPostuler,on_delete=models.CASCADE,related_name="personnesAccorde")
    personnel = models.ForeignKey(Personnel,related_name="sujetsAccorde",on_delete=models.CASCADE)

    class Meta:
        unique_together =['sujetPostuler','personnel']
    def __str__(self):
        return self.valide