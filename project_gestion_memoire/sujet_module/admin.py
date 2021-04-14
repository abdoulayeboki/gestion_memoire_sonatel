from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import  Sujet
from sujet_module.models import  SujetAccorder, SujetPostuler

class SujetAdmin(admin.ModelAdmin):
    list_display   = ('titre', 'description','etatSujet','personnel','createdDate')
admin.site.register(Sujet, SujetAdmin)

class SujetPostulerAdmin(admin.ModelAdmin):
    list_display   = ('motivation', 'cv','datePostuler','personnel','sujet')
admin.site.register(SujetPostuler, SujetPostulerAdmin)

class SujetAccorderAdmin(admin.ModelAdmin):
    list_display   = ('dateAccorde','sujet','personnel')
admin.site.register(SujetAccorder, SujetAccorderAdmin)