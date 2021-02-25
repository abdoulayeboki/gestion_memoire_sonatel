from django.contrib import admin

# Register your models here.
from administration.models import  Etudiant, Promotion,Departement,Filiere,Specialite,Classe,Enseignent

class EtudiantAdmin(admin.ModelAdmin):
     fields = (('nom', 'prenom'),('telephon','email'),('ine','classe','promotion'))
     list_display   = ('nom', 'prenom','telephon','email', 'ine','classe')
     list_filter    = ('classe','classe__specialite','classe__specialite__filiere')
     search_fields  = ('ine', 'nom', 'prenom')
class EnseignentAdmin(admin.ModelAdmin):
     fieldsets = (
        ("Information Personnelle", {
            'fields': ('nom', 'prenom', 'cni')
        }),
        ('Information Suplémentaire', {
            'classes': ('wide ', 'extrapretty'),
            'fields': ('telephon','email','departement'),
        }),
    )
     list_display   = ('nom', 'prenom', 'cni','telephon','email','departement')
     list_filter    = ('departement',)
     search_fields  = ('cni', 'nom', 'prenom')
class ClasseAdmin(admin.ModelAdmin):
     exclude = ('code',)
     list_display   = ('code', 'anneeScolaire', 'specialite')
     list_filter    = ('specialite','specialite__filiere')
     search_fields  = ('code','anneeScolaire')
class SpecialiteAdmin(admin.ModelAdmin):
     exclude = ('code',)
     list_display   = ('code', 'nom', 'filiere')
     list_filter    = ('filiere','filiere__departement')
     search_fields  = ('code', 'nom')
class FiliereAdmin(admin.ModelAdmin):
     exclude = ('code',)
     list_display   = ('code', 'nom', 'departement')
     list_filter    = ('departement',)
     search_fields  = ('code', 'nom')
class DepartementAdmin(admin.ModelAdmin):
     exclude = ('code',)
     list_display   = ('code', 'nom')
     search_fields  = ('code', 'nom')
class PromotionAdmin(admin.ModelAdmin):
     exclude = ('code',)
     list_display   = ('code', 'nom')
     search_fields  = ('code', 'nom')
admin.site.register(Etudiant, EtudiantAdmin)
admin.site.register(Enseignent, EnseignentAdmin)
admin.site.register(Classe, ClasseAdmin)
admin.site.register(Specialite, SpecialiteAdmin)
admin.site.register(Filiere, FiliereAdmin)
admin.site.register(Departement, DepartementAdmin)
admin.site.register(Promotion, PromotionAdmin)


