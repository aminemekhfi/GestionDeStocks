from django.urls import path
from . import views

urlpatterns = [
    path('connexion', views.connexion, name='connexion'),
    path('deconnexion', views.deconnexion, name='deconnexion'),
    path('ajouterUtilisateur', views.ajouterUtilisateur, name='ajouterUtilisateur'),
    path('listeUtilisateur', views.listeUtilisateur, name='listeUtilisateur'),
    path('afficherUtilisateur/<int:id>/', views.afficherUtilisateur, name='afficherUtilisateur'),
]