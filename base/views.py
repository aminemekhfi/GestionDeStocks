from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from django.utils import timezone
from django.contrib import messages
from .models import Stocks_Table, Produit_Table, Fournisseur_Table, Corbeille_Fournisseurs, Corbeille_Produits, Corbeille_Stocks
from .forms import FormulaireAjouterStock, FormulaireAjouterProduit, FormulaireAjouterFournisseur
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User


# Create your views here.

class Home(View):
    def get(self,request):  
            session_expiry = request.session.get_expiry_date()
            current_time = timezone.now()
            request.session.set_expiry(10000) 
            if current_time > session_expiry:
                messages.error(request,"GDStocks : Erreur, session expiré!")
                return redirect('connexion')
            else:
                return render(request,'Acceuil.html',{'user': request.user})
    
class Dashboard(View):
    def get(self, request):  
        nombreStocks = Stocks_Table.objects.count()
        nombreProduits = Produit_Table.objects.count()
        nombreFournisseurs = Fournisseur_Table.objects.count()
        nombreUtilisateurs = User.objects.count()

        dernierStocks = Stocks_Table.objects.order_by('-DateDeCreation')[:5]
        dernierProduits = Produit_Table.objects.order_by('-DateDeCreation')[:5]
        dernierFournisseurs = Fournisseur_Table.objects.order_by('-DateDeCreation')[:5]

        context = {
            'nombreStocks': nombreStocks,
            'nombreProduits': nombreProduits,
            'nombreFournisseurs': nombreFournisseurs,
            'nombreUtilisateurs': nombreUtilisateurs,
            'dernierStocks': dernierStocks,
            'dernierProduits': dernierProduits,
            'dernierFournisseurs': dernierFournisseurs,
        }
        return render(request, 'Dashboard.html', context)
    
class About(View):
    def get(self,request):  
        return render(request,'About.html',{})  
    
class Stocks(View):
    def get(self,request):  
        Stock = Stocks_Table.objects.all()
        return render(request,'Stocks/ListeStocks.html',{'stocks':Stock})
    
class Corbeille(View):
    def get(self,request):  
        FournisseurCorbeille = Corbeille_Fournisseurs.objects.all()
        StocksCorbeille = Corbeille_Stocks.objects.all()
        ProduitsCorbeille = Corbeille_Produits.objects.all()
        return render(request,'Corbeille.html',{'FournisseurCorbeille':FournisseurCorbeille, 'StocksCorbeille':StocksCorbeille, 'ProduitsCorbeille':ProduitsCorbeille})
    
class CreerStocks(View):
    def get(self, request):  
        form = FormulaireAjouterStock()
        return render(request, 'Stocks/CreerStocks.html', {'form': form})

    def post(self, request):
        form = FormulaireAjouterStock(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Stocks')
        return render(request, 'Stocks/CreerStocks.html', {'form': form})
    
class DetailStocks(View):
    def get(self, request, id):
        stock = get_object_or_404(Stocks_Table, id=id)
        return render(request, 'Stocks/AfficherStocks.html', {'stock': stock})

class SupprimerStocks(View):
    def get(self, request, id):
        stock = get_object_or_404(Stocks_Table, id=id)
        return render(request, 'Stocks/SupprimerStocks.html', {'stock': stock})
    
    def post(self, request, id):
        stock = get_object_or_404(Stocks_Table, id=id)
        print("Fournisseur found:", stock)
        form = Corbeille_Stocks.objects.create(
            nomStockCorbeille=stock.nomStock,
            quantiteStockCorbeille=stock.quantiteStock,
            DescriptionStockCorbeille=stock.DescriptionStock,
            dateEntreeStockCorbeille=stock.dateEntreeStock,
            dateExpirationStockCorbeille=stock.dateExpirationStock,
            statutStockCorbeille=stock.statutStock,
            DateDeCreationCorbeille=stock.DateDeCreation
        )
        form.save()
        stock.delete()
        
        return redirect('Stocks')
    
class ModifierStocks(View):
    def get(self, request, id):
        stock = get_object_or_404(Stocks_Table, id=id)
        form = FormulaireAjouterStock(instance=stock)
        return render(request, 'Stocks/ModifierStocks.html', {'form': form, 'stock': stock})

    def post(self, request, id):
        stock = get_object_or_404(Stocks_Table, id=id)
        form = FormulaireAjouterStock(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('DetailStocks', id=stock.id)
        return render(request, 'Stocks/ModifierStocks.html', {'form': form, 'stock': stock})
    
class Produits(View):
    def get(self, request):
        produits = Produit_Table.objects.all() 
        return render(request, 'Produits/ListeProduit.html', {'produits': produits})
    
class DetailProduit(View):
    def get(self, request, id):
        produits = get_object_or_404(Produit_Table, id=id) 
        return render(request, 'Produits/AfficherProduits.html', {'produits': produits})
    
class SupprimerProduit(View):
    def get(self, request, id):
        produits = get_object_or_404(Produit_Table, id=id)
        return render(request, 'Produits/SupprimerProduits.html', {'produits': produits})
    
    def post(self, request, id):
        produits = get_object_or_404(Produit_Table, id=id)
        form = Corbeille_Produits.objects.create(
            nomProduitCorbeille=produits.nomProduit,
            categorieProduitCorbeille=produits.categorieProduit,
            prixProduitCorbeille=produits.prixProduit,
            descriptionProduitCorbeille=produits.descriptionProduit,
            dateExpirationProduitCorbeille=produits.dateExpirationProduit,
            stock=produits.stock,
            fournisseurCorbeille=produits.fournisseur,
            DateDeCreationCorbeille=produits.DateDeCreation,
        )
        form.save()
        produits.delete()
        
        return redirect('Stocks')
    
class ModifierProduit(View):
    def get(self, request, id):
        produits = get_object_or_404(Produit_Table, id=id)
        form = FormulaireAjouterProduit(instance=produits)
        return render(request, 'Produits/ModifierProduit.html', {'form': form, 'produits': produits})

    def post(self, request, id):
        produits = get_object_or_404(Produit_Table, id=id)
        form = FormulaireAjouterProduit(request.POST, instance=produits)
        if form.is_valid():
            form.save()
            return redirect('DetailProduit', id=produits.id)
        return render(request, 'Produits/ModifierProduit.html', {'form': form, 'produits': produits})
   
class CreerProduit(View):
    def get(self, request):  
        form = FormulaireAjouterProduit()
        return render(request, 'Produits/CreerProduit.html', {'form': form})

    def post(self, request):
        form = FormulaireAjouterProduit(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Produits')
        return render(request, 'Produits/CreerProduit.html', {'form': form})
    
class Fournisseur(View):
    def get(self,request):  
        fournisseur = Fournisseur_Table.objects.all()
        return render(request,'Fournisseurs/listeFournisseurs.html',{'fournisseur':fournisseur})
    
class DetailFournisseur(View):
    def get(self, request, id):
        fournisseur = get_object_or_404(Fournisseur_Table, id=id) 
        return render(request, 'Fournisseurs/AfficherFournisseur.html', {'fournisseur': fournisseur})
    
class CreerFournisseur(View):
    def get(self, request):  
        form = FormulaireAjouterFournisseur()
        return render(request, 'Fournisseurs/CreerFournisseur.html', {'form': form})

    def post(self, request):
        form = FormulaireAjouterFournisseur(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Fournisseur')
        return render(request, 'Fournisseurs/CreerFournisseur.html', {'form': form})
    
class ModifierFournisseur(View):
    def get(self, request, id):
        fournisseur = get_object_or_404(Fournisseur_Table, id=id)
        form = FormulaireAjouterFournisseur(instance=fournisseur)
        return render(request, 'Fournisseurs/ModifierFournisseur.html', {'form': form, 'fournisseur': fournisseur})

    def post(self, request, id):
        fournisseur = get_object_or_404(Fournisseur_Table, id=id)
        form = FormulaireAjouterFournisseur(request.POST, instance=fournisseur)
        if form.is_valid():
            form.save()
            return redirect('DetailFournisseur', id=fournisseur.id)
        return render(request, 'Fournisseurs/ModifierFournisseur.html', {'form': form, 'fournisseur': fournisseur})

class SupprimerFournisseur(View):
    def get(self, request, id):
        fournisseur = get_object_or_404(Fournisseur_Table, id=id)
        return render(request, 'Fournisseurs/SupprimerFournisseur.html', {'fournisseur': fournisseur})
    
    def post(self, request, id):
        fournisseur = get_object_or_404(Fournisseur_Table, id=id)
        print("Fournisseur found:", fournisseur)
        form = Corbeille_Fournisseurs.objects.create(
            nomFournisseurCorbeille=fournisseur.nomFournisseur,
            dateDeNaissanceFournisseurCorbeille=fournisseur.dateDeNaissanceFournisseur,
            telephoneFournisseurCorbeille=fournisseur.telephoneFournisseur,
            adresseFournisseurCorbeille=fournisseur.adresseFournisseur,
            DateDeCreationCorbeille=fournisseur.DateDeCreation
        )
        form.save()
        fournisseur.delete()
        
        return redirect('Fournisseur')
    


