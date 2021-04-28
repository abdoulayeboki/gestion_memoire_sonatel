from django.db import models
from administration.models import  Personnel
from sujet_module.models import Sujet
from django.core.exceptions import PermissionDenied
from django.dispatch import receiver
from django.db.models.signals import pre_delete,post_save,pre_save
# Create your models here.
class Encadrement(models.Model):
    appreciation = models.CharField(max_length=255)
    dateDebutEncadrement = models.DateTimeField(auto_now_add=True)
    dateFinEncadrement = models.DateTimeField(null=True)
    sujet = models.OneToOneField(Sujet,on_delete=models.CASCADE, related_name="encadrement")
    
    def __str__(self):
        return self.sujet.titre  
    def save(self, *args, **kwargs):
        if  self.sujet.etatSujet != "VALIDE":
            raise PermissionDenied("Imposible! Le sujet n'est pas valide")
        else:
            super().save(*args, **kwargs)
    
class Evenement(models.Model):
    titre = models.CharField(max_length=255)
    duree = models.CharField(max_length=255)
    description = models.TextField()
    dateEvenement = models.DateTimeField()
    encadrement = models.ForeignKey(Encadrement,on_delete=models.CASCADE, related_name="evenements")
    owner = models.ForeignKey(Personnel,on_delete=models.CASCADE, related_name="evenements")


def upload_path(instance, filename):
    return '/'.join(['ressource',str(instance.encadrement.id), filename])
class Ressource(models.Model):
    titre = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(blank=True, null=True, upload_to=upload_path) 
    encadrement = models.ForeignKey(Encadrement,on_delete=models.CASCADE, related_name="ressources")
    owner = models.ForeignKey(Personnel,on_delete=models.CASCADE, related_name="ressources")
