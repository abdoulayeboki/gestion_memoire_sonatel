from django.db import models

# Create your models here.
class Departement(models.Model):
    code = models.CharField(max_length=25)
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
class Enseignent(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    cni = models.CharField(max_length=20, unique=True)
    grade = models.CharField(max_length=100)
    specialite= models.CharField(max_length=100)
    telephon = models.CharField(max_length=18,default=None)
    email = models.CharField(max_length=100,default=None)
    departement = models.ForeignKey(Departement, related_name="professeurs",on_delete=models.CASCADE)

    class Meta:
        ordering: ['nom']


    def __str__(self):
        return self.nom
class Promotion(models.Model):
    code = models.CharField(max_length=25)
    nom = models.CharField(max_length=100)
    def __str__(self):
        return self.nom

class Filiere(models.Model):
    code = models.CharField(max_length=25)
    nom = models.CharField(max_length=100)
    departement = models.ForeignKey(Departement, related_name="filieres",on_delete=models.CASCADE)
    def __str__(self):
        return self.nom 

class Specialite(models.Model):
    list_niveau = (("BTS","BTS"),("L3","licence 3"),("M2","Master 2"), ("T1","These 1"),("T2","These 2"),("T3","These 3"))
    code = models.CharField(max_length=25)
    nom = models.CharField(max_length=100)
    niveau = models.CharField(max_length=10, choices= list_niveau, default="M2")
    filiere = models.ForeignKey(Filiere, related_name="specialites",on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Classe(models.Model):
    list_year = (("2020-2021","2020-2021"),("2021-2022","2021-2022"),("2022-2023","2022-2023"),("2023-2024","2023-2024"),("2024-2025","2024-2025"),("2025-2026","2025-2026"))
    code = models.CharField(max_length=25,unique=True)
    anneeScolaire = models.CharField(max_length=9, choices=list_year, default="2021")
    specialite = models.ForeignKey(Specialite, related_name="classes",on_delete=models.CASCADE)
    class Meta:
        unique_together = ['anneeScolaire', 'specialite']
    def __str__(self):
        return "%s   %s"% (self.specialite, self.anneeScolaire)

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    ine = models.CharField(max_length=7)
    telephon = models.CharField(max_length=18,default=None)
    email = models.CharField(max_length=100,default=None)
    promotion = models.ForeignKey(Promotion, related_name="etudiants",on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, related_name="etudiants",on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "%s %s" % (self.ine, self.nom)
