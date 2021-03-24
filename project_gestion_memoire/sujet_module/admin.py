from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import  Sujet
from sujet_module.models import EtudiantPostuler,EnseignantPostuler

class SujetAdmin(admin.ModelAdmin):
    list_display   = ('titre', 'description','etatSujet','owner','createdDate')
admin.site.register(Sujet, SujetAdmin)

class EtudiantPostulerAdmin(admin.ModelAdmin):
    list_display   = ('motivation', 'cv','datePostuler','etudiant','sujet')
admin.site.register(EtudiantPostuler, EtudiantPostulerAdmin)

class EnseignantPostulerAdmin(admin.ModelAdmin):
    list_display   = ('motivation','datePostuler','enseignant','sujet')
admin.site.register(EnseignantPostuler, EnseignantPostulerAdmin)