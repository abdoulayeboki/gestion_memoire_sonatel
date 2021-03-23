from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from sujet_module.models import  Sujet

class SujetAdmin(admin.ModelAdmin):
    #  exclude =('owner',)
     list_display   = ('titre', 'description','etatSujet','owner','createdDate')
admin.site.register(Sujet, SujetAdmin)