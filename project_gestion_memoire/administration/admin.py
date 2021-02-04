from django.contrib import admin

# Register your models here.
from administration.models import  Etudiant, Promotion,Departement,Filiere,Specialite,Classe

admin.site.register([Etudiant, Promotion,Departement,Filiere,Specialite,Classe])