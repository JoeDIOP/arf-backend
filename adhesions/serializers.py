from rest_framework import serializers
from .models import Adhesion

class AdhesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adhesion
        fields = [
            'id',
            'nom_prenom',
            'email',
            'telephone',
            'village_quartier',
            'domaine_participation',
            'motivations',
            'date_inscription',
            'statut',
            'consentement_rgpd',
            'consentement_newsletter',
        ]
        read_only_fields = ['id', 'date_inscription', 'statut']
