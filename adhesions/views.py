from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from .models import Adhesion
from .serializers import AdhesionSerializer
import json

class AdhesionViewSet(viewsets.ModelViewSet):
    queryset = Adhesion.objects.all()
    serializer_class = AdhesionSerializer
    
    def perform_create(self, serializer):
        """Créer une adhésion et envoyer les emails"""
        adhesion = serializer.save()
        
        # Envoyer email à l'adhérent
        self.send_confirmation_email(adhesion)
        
        # Envoyer email à l'équipe ARF
        self.send_notification_email(adhesion)
    
    def send_confirmation_email(self, adhesion):
        """Email de confirmation à l'adhérent"""
        subject = "Bienvenue à l'Alliance pour le Renouveau de Fandne"
        message = f"""
Bonjour {adhesion.nom_prenom},

Merci de nous avoir rejoints ! Votre adhésion a été enregistrée avec succès.

Nous avons reçu :
- Email : {adhesion.email}
- Téléphone : {adhesion.telephone}
- Village/Quartier : {adhesion.village_quartier}
- Domaine : {adhesion.get_domaine_participation_display()}

L'équipe ARF vous contactera bientôt pour les prochaines étapes.

Bienvenue dans le mouvement !

---
Alliance pour le Renouveau de Fandne
        """
        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [adhesion.email],
                fail_silently=False,
            )
        except Exception as e:
            print(f"Erreur envoi email : {e}")
    
    def send_notification_email(self, adhesion):
        """Email de notification à l'équipe ARF"""
        subject = f"[ARF] Nouvelle adhésion : {adhesion.nom_prenom}"
        message = f"""
Nouvelle adhésion enregistrée !

Nom & Prénom : {adhesion.nom_prenom}
Email : {adhesion.email}
Téléphone : {adhesion.telephone}
Village/Quartier : {adhesion.village_quartier}
Domaine : {adhesion.get_domaine_participation_display()}
Motivations : {adhesion.motivations}

Date inscription : {adhesion.date_inscription}
Statut : {adhesion.get_statut_display()}
        """
        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ARF_ADMIN_EMAIL],  # À configurer dans .env
                fail_silently=False,
            )
        except Exception as e:
            print(f"Erreur envoi email admin : {e}")


@api_view(['GET'])
def adhesion_stats(request):
    """Endpoint de stats (optionnel)"""
    total = Adhesion.objects.count()
    par_domaine = {}
    for domaine, label in Adhesion.DOMAINES_CHOICES:
        par_domaine[label] = Adhesion.objects.filter(domaine_participation=domaine).count()
    
    return Response({
        'total': total,
        'par_domaine': par_domaine,
    })
