from django.db import models
from enum import Enum
from django.contrib.auth.models import User
from django.db.models.functions import Coalesce
from administration.models import  Etudiant, Enseignent
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
    postulants = models.ManyToManyField(Etudiant, through='EtudiantPostuler',related_name="sujetsPostuler")
    EnseignantPostulant = models.ManyToManyField(Enseignent, through='EnseignantPostuler',related_name="sujetsPostuler")
    EnseignantValide = models.ManyToManyField(Enseignent, through='SujetValide',related_name="sujetsValide")
    EnseignantAccorde = models.ManyToManyField(Enseignent, through='SujetAccorde',related_name="sujetsAccorde")

    def __str__(self):
        return self.titre
    
    # def save(self,force_update=True, *args, **kwargs):
    #     self.etatSujet = "VALIDE"
    #     super().save(*args, **kwargs)  

class EtudiantPostuler(models.Model):
    datePostuler = models.DateTimeField(auto_now_add=True)
    motivation = models.TextField()
    cv = models.CharField(max_length=255)
    etudiant = models.ForeignKey(Etudiant,on_delete=models.CASCADE)
    sujet = models.ForeignKey(Sujet,on_delete=models.CASCADE)

    class Meta:
        unique_together =['etudiant','sujet']

    

class EnseignantPostuler(models.Model):
    datePostuler = models.DateTimeField(auto_now_add=True)
    motivation = models.TextField()
    enseignant = models.ForeignKey(Enseignent,on_delete=models.CASCADE)
    sujet = models.ForeignKey(Sujet,on_delete=models.CASCADE)

    class Meta:
        unique_together =['enseignant','sujet']

class SujetValide(models.Model):
    validateDate = models.DateTimeField(auto_now_add=True)
    enseignant = models.ForeignKey(Enseignent,on_delete=models.CASCADE)
    sujet = models.ForeignKey(Sujet,on_delete=models.CASCADE)
    etudiant = models.OneToOneField(Etudiant,related_name="sujetValide",on_delete=models.CASCADE)

    class Meta:
        unique_together =['enseignant','sujet','etudiant']

class SujetAccorde(models.Model):
    accordeDate = models.DateTimeField(auto_now_add=True)
    enseignant = models.ForeignKey(Enseignent,on_delete=models.CASCADE)
    sujet = models.ForeignKey(Sujet,on_delete=models.CASCADE)
    etudiant = models.ForeignKey(Etudiant,related_name="sujetsAccorde",on_delete=models.CASCADE)

    class Meta:
        unique_together =[['enseignant','sujet','etudiant'],['sujet','etudiant'],['enseignant','sujet']]