from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdhesionViewSet, adhesion_stats

router = DefaultRouter()
router.register(r'adhesions', AdhesionViewSet, basename='adhesion')

urlpatterns = [
    path('', include(router.urls)),
    path('adhesions/stats/', adhesion_stats, name='adhesion-stats'),
]
