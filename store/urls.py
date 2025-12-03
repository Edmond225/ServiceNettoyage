from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),

    # Racine du site → page d'accueil
    path('', views.home, name='home'),

    # Autres pages si nécessaire
    path('about/', views.about, name='about'),
    path('demande_devis/', views.demande_devis, name='demande_devis'),
    path('detail/', views.detail, name='detail'),
    path('servicenettoyage/', views.servicenettoyage, name='servicenettoyage'),
]
