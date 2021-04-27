from django.contrib import admin
from .models import Encadrement
# Register your models here.

class EncadrementAdmin(admin.ModelAdmin):
    # exclude=("dateFinEncadrement",)
    list_display   = ('appreciation','dateDebutEncadrement','dateFinEncadrement','sujet')
admin.site.register(Encadrement, EncadrementAdmin)