from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home.as_view(),name='Home'),   
    path('About/',views.About.as_view(),name='About'),   
    path('Dashboard/',views.Dashboard.as_view(),name='Dashboard'),  
    path('Corbeille/',views.Corbeille.as_view(),name='Corbeille'),  
    path('Restaurer/',views.Corbeille.as_view(),name='Restaurer'),  

    path('stocks/',views.Stocks.as_view(),name='Stocks'),     
    path('CreerStock/',views.CreerStocks.as_view(),name='CreerStocks'),  
    path('stocks/<int:id>/', views.DetailStocks.as_view(), name='DetailStocks'),
    path('stocks/<int:id>/delete/', views.SupprimerStocks.as_view(), name='SupprimerStocks'),
    path('stocks/<int:id>/update/', views.ModifierStocks.as_view(), name='ModifierStocks'),

    path('Produits/',views.Produits.as_view(),name='Produits'),  
    path('CreerProduit/',views.CreerProduit.as_view(),name='CreerProduit'),
    path('Produits/<int:id>/', views.DetailProduit.as_view(), name='DetailProduit'),  
    path('Produits/<int:id>/delete/', views.SupprimerProduit.as_view(), name='SupprimerProduit'),
    path('Produits/<int:id>/update/', views.ModifierProduit.as_view(), name='ModifierProduit'),

    path('Fournisseurs/',views.Fournisseur.as_view(),name='Fournisseur'), 
    path('Fournisseurs/<int:id>/', views.DetailFournisseur.as_view(), name='DetailFournisseur'),   
    path('CreerFournisseur/',views.CreerFournisseur.as_view(),name='CreerFournisseur'),  
    path('Fournisseurs/<int:id>/update/', views.ModifierFournisseur.as_view(), name='ModifierFournisseur'),
    path('Fournisseurs/<int:id>/delete/', views.SupprimerFournisseur.as_view(), name='SupprimerFournisseur'),
]