from django.db import models
from enum import Enum
from django.contrib.auth.models import User
from django.db.models.functions import Coalesce
from administration.models import Enseignent, Etudiant, Personnel
from django.http import Http404 , HttpResponse
from django.core.exceptions import PermissionDenied
from django.dispatch import receiver
from django.db.models.signals import pre_delete,post_save,pre_save
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
    personnelValider = models.ManyToManyField(Personnel, through='SujetValider')

    def __str__(self):
        return self.titre
    
    def save(self, *args, **kwargs):
        if not self.personnel:
            raise PermissionDenied("Imposible! Vous n'etes pas un personnel ")
        else:
            super().save(*args, **kwargs)


def upload_path(instance, filename):
    return '/'.join(['file',str(instance.sujet.id),str(instance.personnel.id), filename])
class SujetPostuler(models.Model):
    datePostuler = models.DateTimeField(auto_now_add=True)
    motivation = models.TextField()
    personnel = models.ForeignKey(Personnel,on_delete=models.CASCADE)
    sujet = models.ForeignKey(Sujet,on_delete=models.CASCADE)
    file_cv = models.FileField(blank=True, null=True, upload_to=upload_path) 
    class Meta:
        unique_together =['personnel','sujet']
    def __str__(self):
        return  self.cv
    def save(self, *args, **kwargs):
        # on verifie si l'etudiant n'a pas un sujet valide
        if self.personnel.profil == "ETUDIANT":
            if len(SujetValider.objects.filter(personnel=self.personnel.id)) > 0:
                raise PermissionDenied("Imposible! vous ne pouvez pas postuler à ce sujet, car vous avez un sujet valide")

        if self.personnel.profil == self.sujet.personnel.profil:
            raise PermissionDenied("Imposible! Vous avez le meme profile")
        elif (self.personnel.profil == "AUTRE" and self.sujet.personnel.profil =="ENSEIGNANT"):
            raise  PermissionDenied("Imposible! Vous ne pouvez pas postuler à ce sujet, car vous fetes parti de l'administration")
        else:
            super().save(*args, **kwargs)

class SujetAccorder(models.Model):
    dateAccorde = models.DateTimeField(auto_now_add=True)
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


class SujetValider(models.Model):
    dateValider = models.DateTimeField(auto_now_add=True)
    sujet = models.ForeignKey(Sujet,on_delete=models.CASCADE)
    personnel = models.ForeignKey(Personnel,on_delete=models.CASCADE)

    class Meta:
        unique_together =['sujet','personnel']
    # def __str__(self):
    #     return self.sujet
    
    def save(self, *args, **kwargs):
        sujet = Sujet.objects.get(pk=self.sujet.id) #on recupere le sujet concerné
        Sujet.objects.filter(pk=self.sujet.id).update(etatSujet="VALIDE") # Mettre a jour l'état du sujet
        Personnel.objects.filter(pk=self.personnel.id).update(nbr_sujet_valide=(self.personnel.nbr_sujet_valide +1))
        list_idPersonne = sujet.personnelAccorder.values_list("id",flat=True) # on recupere les personnes accordees
        if self.personnel.id not in list_idPersonne:                          # on verifie si le personnel est dans la liste
            raise PermissionDenied("Imposible! Vous avez n'etes pas accordé à ce sujet")
        if len(SujetValider.objects.filter(personnel__id=self.personnel.id,personnel__profil="ETUDIANT")) > 0:
            raise PermissionDenied("Imposible!, l'etudiant a déjà n sujet valide")
        # else if self.sujet.personnel.id != 
        else:
            super().save(*args, **kwargs)


# écoute le signal lors de suppression d'un SujetAccorder
@receiver(pre_delete, sender=SujetAccorder)
def update_etatSujet(sender, instance, **kwargs):
    if len(SujetAccorder.objects.filter(sujet=instance.sujet.id)) <= 1:  # on verifie si le sujet n'est pas accorde à d'autre personne
        Sujet.objects.filter(pk=instance.sujet.id).update(etatSujet="PROPOSE") # on change son état s'il n'es accorde à personne


@receiver(pre_save, sender=SujetAccorder)
def pre_save_SujetAccorder(sender, instance, **kwargs): 
        if not instance._state.adding: # s'il s'agit d'un update
            if len(SujetAccorder.objects.filter(personnel=instance.personnel.id,personnel__profil="ETUDIANT",valide=True)) > 0:
                raise Http404("Imposible! l'etudiant a déjà un sujet validé")
            else:
                if instance.sujet.etatSujet=="VALIDE":
                    Sujet.objects.filter(pk=instance.sujet.id).update(etatSujet="ACCORDE")
                elif instance.sujet.etatSujet=="ACCORDE":
                    Sujet.objects.filter(pk=instance.sujet.id).update(etatSujet="VALIDE")
        else: # s'il s'agit d'une insertion
            pass