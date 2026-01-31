from django.contrib import admin
from .models import Adhesion

@admin.register(Adhesion)
class AdhesionAdmin(admin.ModelAdmin):
    list_display = ('nom_prenom', 'email', 'village_quartier', 'domaine_participation', 'date_inscription', 'statut')
    list_filter = ('domaine_participation', 'statut', 'date_inscription')
    search_fields = ('nom_prenom', 'email', 'village_quartier')
    ordering = ('-date_inscription',)
    readonly_fields = ('date_inscription',)
    fieldsets = (
        (None, {
            'fields': ('nom_prenom', 'email', 'telephone', 'village_quartier', 'domaine_participation', 'statut')
        }),
        ('Dates', {
            'fields': ('date_inscription',),
            'classes': ('collapse',),
        }),
    )
