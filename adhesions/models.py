from django.db import models
from django.utils import timezone

class Adhesion(models.Model):
    DOMAINES_CHOICES = [
        ('economie', 'Développement économique'),
        ('education', 'Éducation et Formation'),
        ('sante', 'Santé et Bien-être'),
        ('environnement', 'Environnement et Durabilité'),
        ('cohesion', 'Cohésion Sociale'),
        ('autre', 'Autre'),
    ]
    
    STATUT_CHOICES = [
        ('nouveau', 'Nouveau'),
        ('valide', 'Validé'),
        ('attente', 'En attente de validation'),
        ('refuse', 'Refusé'),
    ]
    
    # Champs du formulaire
    nom_prenom = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=20, blank=True)
    village_quartier = models.CharField(max_length=255)
    domaine_participation = models.CharField(
        max_length=50,
        choices=DOMAINES_CHOICES,
        default='autre'
    )
    motivations = models.TextField(blank=True)
    
    # Métadonnées
    date_inscription = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='nouveau'
    )
    
    # RGPD
    consentement_rgpd = models.BooleanField(default=False)
    consentement_newsletter = models.BooleanField(default=False)
    date_consentement = models.DateTimeField(null=True, blank=True)
    
    # Métadonnées système
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    
    class Meta:
        ordering = ['-date_inscription']
        verbose_name = 'Adhésion'
        verbose_name_plural = 'Adhésions'
    
    def __str__(self):
        return f"{self.nom_prenom} - {self.email}"
