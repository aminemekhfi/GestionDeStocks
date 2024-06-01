from django.db import models

class Stocks_Table(models.Model):
    nomStock = models.CharField(max_length=50)
    quantiteStock = models.IntegerField()
    DescriptionStock = models.CharField(max_length=200)
    dateEntreeStock = models.DateField()
    dateExpirationStock = models.DateField()
    statutStock = models.CharField(max_length=30, choices=[
        ('disponible', 'Disponible'),
        ('expire', 'Expire'),
        ('commande', 'Commande'),
    ])
    DateDeCreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomStock

class Fournisseur_Table(models.Model):
    nomFournisseur = models.CharField(max_length=50)
    dateDeNaissanceFournisseur = models.DateField()
    telephoneFournisseur = models.CharField(max_length=50)
    adresseFournisseur = models.CharField(max_length=50)
    DateDeCreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomFournisseur

class Produit_Table(models.Model):
    nomProduit = models.CharField(max_length=50)
    categorieProduit = models.CharField(max_length=100)
    prixProduit = models.FloatField()
    descriptionProduit = models.CharField(max_length=200)
    dateExpirationProduit = models.DateField()
    stock = models.ForeignKey(Stocks_Table, on_delete=models.CASCADE, related_name='produits')
    fournisseur = models.ForeignKey(Fournisseur_Table, on_delete=models.CASCADE, related_name='produits')
    DateDeCreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomProduit

class Corbeille_Stocks(models.Model):
    nomStockCorbeille = models.CharField(max_length=50)
    quantiteStockCorbeille = models.IntegerField()
    DescriptionStockCorbeille = models.CharField(max_length=200)
    dateEntreeStockCorbeille = models.DateField()
    dateExpirationStockCorbeille = models.DateField()
    statutStockCorbeille = models.CharField(max_length=30, choices=[
        ('disponible', 'Disponible'),
        ('expire', 'Expire'),
        ('commande', 'Commande'),
    ])
    DateDeCreationCorbeille = models.DateTimeField(auto_now_add=True)
    dateSupressionStocks = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.nomStockCorbeille)

class Corbeille_Produits(models.Model):
    nomProduitCorbeille = models.CharField(max_length=50)
    categorieProduitCorbeille = models.CharField(max_length=100)
    prixProduitCorbeille = models.FloatField()
    descriptionProduitCorbeille = models.CharField(max_length=200)
    dateExpirationProduitCorbeille = models.DateField()
    stock = models.ForeignKey(Stocks_Table, on_delete=models.CASCADE, related_name='corbeille_produits_stock')
    fournisseurCorbeille = models.ForeignKey(Fournisseur_Table, on_delete=models.CASCADE, related_name='corbeille_produits_fournisseur')
    DateDeCreationCorbeille = models.DateTimeField(auto_now_add=True)
    dateSupressionProduitsCorbeille = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.nomProduitCorbeille)

class Corbeille_Fournisseurs(models.Model):
    nomFournisseurCorbeille = models.CharField(max_length=50)
    dateDeNaissanceFournisseurCorbeille = models.DateField()
    telephoneFournisseurCorbeille = models.CharField(max_length=50)
    adresseFournisseurCorbeille = models.CharField(max_length=50)
    DateDeCreationCorbeille = models.DateTimeField(auto_now_add=True)
    dateSupressionFournisseurs = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.nomFournisseurCorbeille)
