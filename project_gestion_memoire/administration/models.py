from django.db import models
from enum import Enum
from django.contrib.auth.models import User

# Create your models here.
class Departement(models.Model):
    code = models.CharField(max_length=25,unique=True)
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom
class ProfilEnumeration(Enum):
    ETUDIANT = "ETUDIANT"
    ENSEIGNANT = "ENSEIGNANT"
    AUTRE  = "AUTRE"
class Personnel(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    cni = models.CharField(max_length=20, unique=True)
    telephon = models.CharField(max_length=18,default=None)
    email = models.CharField(max_length=100)
    profil = models.CharField(max_length=20,
    choices= [(tag.value, tag.value) for tag in ProfilEnumeration],default='AUTRE')
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="personnel",null=True, unique=True)

    class Meta:
        unique_together = [['cni'],['user']]
    def __str__(self):
        return self.nom
    def save(self, *args, **kwargs):
        # self.profil = 'AUTRE'
        super().save(*args, **kwargs) 
class Enseignent(Personnel):
    grade = models.CharField(max_length=100)
    specialite= models.CharField(max_length=100)
    departement = models.ForeignKey(Departement, related_name="professeurs",on_delete=models.CASCADE)

    class Meta:
        ordering: ['nom']

    def save(self, *args, **kwargs):
        self.profil ='ENSEIGNANT'
        super().save(*args, **kwargs) 
    def __str__(self):
        return str(self.nom)
class Promotion(models.Model):
    code = models.CharField(max_length=25, unique=True)
    nom = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        list_nom = self.nom.split(' ')
        code = [n[0:5].upper() for n in list_nom]
        self.code = '_'.join(code)
        super().save(*args, **kwargs)  # Call the "real" save() method.
    def __str__(self):
        return self.nom

class Filiere(models.Model):
    code = models.CharField(max_length=25,unique=True)
    nom = models.CharField(max_length=100)
    departement = models.ForeignKey(Departement, related_name="filieres",on_delete=models.CASCADE)

    # on redefinit la methode save pour pouvoir attribue le code à une filiere
    def save(self, *args, **kwargs):
        list_nom = self.nom.split(' ')
        if len(list_nom) > 1:
            nom = [n[0:1].upper() for n in list_nom if len(n) >= 3]
            self.code = ''.join(nom)
        else:
            self.code = ''.join(self.nom)
        super().save(*args, **kwargs)  # Call the "real" save() method.
    def __str__(self):
        return self.nom 

class Specialite(models.Model):
    list_niveau = (("BTS","BTS"),("L3","licence 3"),("M2","Master 2"), ("T1","These 1"),("T2","These 2"),("T3","These 3"))
    code = models.CharField(max_length=25, unique=True)
    nom = models.CharField(max_length=100,unique=True)
    niveau = models.CharField(max_length=10, choices= list_niveau, default="M2")
    filiere = models.ForeignKey(Filiere, related_name="specialites",on_delete=models.CASCADE)

     # on redefinit la methode save pour pouvoir attribue le code à une filiere
    def save(self, *args, **kwargs):
        list_nom = self.nom.split(' ')
        if len(list_nom) > 1:
            nom = [n[0:1].upper() for n in list_nom if len(n) >= 3]
            self.code = ''.join(nom)
        else:
            self.code = ''.join(self.nom)
        super().save(*args, **kwargs)  # Call the "real" save() method.
    def __str__(self):
        return self.nom

class Classe(models.Model):
    list_year = (("2020-2021","2020-2021"),("2021-2022","2021-2022"),("2022-2023","2022-2023"),("2023-2024","2023-2024"),("2024-2025","2024-2025"),("2025-2026","2025-2026"))
    code = models.CharField(max_length=25,unique=True)
    anneeScolaire = models.CharField(max_length=9, choices=list_year, default="2021")
    specialite = models.ForeignKey(Specialite, related_name="classes",on_delete=models.CASCADE)

     # on redefinit la methode save pour pouvoir attribue le code à une filiere
    def save(self, *args, **kwargs):
        self.code = (self.specialite.code + '_' + self.anneeScolaire).upper()
        super().save(*args, **kwargs)  # Call the "real" save() method.
    class Meta:
        unique_together = ['anneeScolaire', 'specialite']
    def __str__(self):
        return "%s   %s"% (self.specialite, self.anneeScolaire)

class Etudiant(Personnel):
    ine = models.CharField(max_length=7, unique=True)
    promotion = models.ForeignKey(Promotion, related_name="etudiants",on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, related_name="etudiants",on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.ine)

    class Meta:
        ordering: ['ine']
    
    def save(self, *args, **kwargs):
        self.profil = 'ETUDIANT'
        super().save(*args, **kwargs) 