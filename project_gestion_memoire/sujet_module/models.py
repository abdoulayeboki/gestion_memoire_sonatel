from django.db import models
from enum import Enum
from django.contrib.auth.models import User
from django.db.models.functions import Coalesce
from administration.models import Enseignent, Etudiant, Personnel
from django.http import Http404 , HttpResponse
from django.core.exceptions import PermissionDenied
from django.dispatch import receiver
from django.db.models.signals import pre_delete
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
    personnel = models.ForeignKey(Personnel,on_delete=models.CASCADE,related_name="mesSujets")
    etatSujet = models.CharField(max_length=10,
            choices= [(tag.value, tag.value) for tag in EtatSujetEnumeration], default="PROPOSE")
    personnelPostuler = models.ManyToManyField(Personnel, through='SujetPostuler',related_name="sujetsPostuler")
    personnelAccorder = models.ManyToManyField(Personnel, through='SujetAccorder',related_name="sujetsAccorder")

    def __str__(self):
        return self.titre
    
    def save(self, *args, **kwargs):
        if not self.personnel:
            raise PermissionDenied("Imposible! Vous n'etes pas un personnel ")
        else:
            super().save(*args, **kwargs)


class SujetPostuler(models.Model):
    datePostuler = models.DateTimeField(auto_now_add=True)
    motivation = models.TextField()
    cv = models.CharField(max_length=255)
    personnel = models.ForeignKey(Personnel,on_delete=models.CASCADE)
    sujet = models.ForeignKey(Sujet,on_delete=models.CASCADE)
    class Meta:
        unique_together =['personnel','sujet']
    def __str__(self):
        return  self.cv
    def save(self, *args, **kwargs):
        if self.personnel.profil == self.sujet.personnel.profil:
            raise PermissionDenied("Imposible! Vous avez le meme profile")
        elif (self.personnel.profil == "AUTRE" and self.sujet.personnel.profil =="ENSEIGNANT"):
            raise  PermissionDenied("Imposible! Vous ne pouvez pas postuler à ce sujet, car vous fetes parti de l'administration")
        else:
            super().save(*args, **kwargs)

class SujetAccorder(models.Model):
    dateAccorde = models.DateTimeField(auto_now_add=True)
    valide = models.BooleanField(default=False)
    sujet = models.ForeignKey(Sujet,on_delete=models.CASCADE)
    personnel = models.ForeignKey(Personnel,on_delete=models.CASCADE)

    class Meta:
        unique_together =['sujet','personnel']
    def __str__(self):
        return self.valide
    
    def save(self, *args, **kwargs):
        sujet = Sujet.objects.get(pk=self.sujet.id) #on recupere le sujet concerné
        Sujet.objects.filter(pk=self.sujet.id).update(etatSujet="ACCORDE") # Mettre a jour l'état du sujet
        list_idPersonne = sujet.personnelPostuler.values_list("id",flat=True) # on recupere les postulant
        if self.personnel.id not in list_idPersonne:                          # on verifie si le personnel est dans la liste
            raise PermissionDenied("Imposible! Vous avez n'avez pas postulé à ce sujet")
        # else if self.sujet.personnel.id != 
        else:
            super().save(*args, **kwargs)
@receiver(pre_delete, sender=SujetAccorder)
def update_etatSujet(sender, instance, **kwargs):
    if len(SujetAccorder.objects.filter(sujet=instance.sujet.id)) <= 1:
        Sujet.objects.filter(pk=instance.sujet.id).update(etatSujet="PROPOSE") 