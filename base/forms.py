from django import forms
from .models import Stocks_Table, Produit_Table, Fournisseur_Table

class FormulaireAjouterStock(forms.ModelForm):
    nomStock = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer le nom du stock'}))
    quantiteStock = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer la quantité du stock'}))
    DescriptionStock = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer la description du stock'}))
    dateEntreeStock = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'placeholder':'Entrer la date dentrée du stock'}))
    dateExpirationStock = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'placeholder':'Entrer la date dexpiration du stock'}))
    statutStock = forms.ChoiceField(choices=[
        ('disponible', 'Disponible'),
        ('expire', 'Expire'),
        ('commande', 'Commande'),
    ], widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Stocks_Table
        fields = ['nomStock', 'quantiteStock', 'DescriptionStock', 'dateEntreeStock', 'dateExpirationStock', 'statutStock']



class FormulaireAjouterFournisseur(forms.ModelForm):
    nomFournisseur = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer le nom du fournisseur'}))
    dateDeNaissanceFournisseur = forms.DateField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Donne la date de naissance du fournisseur'}))
    telephoneFournisseur = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer le téléphone du fournisseur'}))
    adresseFournisseur = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer adresse du fournisseur'}))
    class Meta:
        model = Fournisseur_Table
        fields = ['nomFournisseur', 'dateDeNaissanceFournisseur', 'telephoneFournisseur', 'adresseFournisseur']



class FormulaireAjouterProduit(forms.ModelForm):
    nomProduit = forms.CharField(label="Nom de produit ",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer le nom du Produit'}))
    categorieProduit = forms.ChoiceField(choices=[
        ('Alimentation', 'alimentation'),
        ('Maison et Jardin', 'maison et jardin'),
        ('Mode et Accessoires', 'mode et accessoires'),
        ('Électronique ', 'electronique '),
        ('Santé et Beauté', 'santé et beauté'),
        ('Loisirs et Divertissements', 'loisirs et divertissements'),
        ('Automobile ', 'automobile'),
    ], widget=forms.Select(attrs={'class': 'form-control'}))
    prixProduit = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer la description du Produit'}))
    descriptionProduit = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer la date dentrée du Produit'}))
    dateExpirationProduit = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'placeholder':'Entrer la date dexpiration du Produit'}))
    stock = forms.ModelChoiceField(queryset=Stocks_Table.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    fournisseur = forms.ModelChoiceField(queryset=Fournisseur_Table.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Produit_Table
        fields = ['nomProduit', 'categorieProduit', 'prixProduit', 'descriptionProduit', 'dateExpirationProduit', 'stock', 'fournisseur']


