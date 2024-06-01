# Generated by Django 5.0.6 on 2024-05-30 15:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corbeille_Fournisseurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomFournisseurCorbeille', models.CharField(max_length=50)),
                ('dateDeNaissanceFournisseurCorbeille', models.DateField()),
                ('telephoneFournisseurCorbeille', models.CharField(max_length=50)),
                ('adresseFournisseurCorbeille', models.CharField(max_length=50)),
                ('DateDeCreationCorbeille', models.DateTimeField(auto_now_add=True)),
                ('dateSupressionFournisseurs', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Corbeille_Stocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomStockCorbeille', models.CharField(max_length=50)),
                ('quantiteStockCorbeille', models.IntegerField()),
                ('DescriptionStockCorbeille', models.CharField(max_length=200)),
                ('dateEntreeStockCorbeille', models.DateField()),
                ('dateExpirationStockCorbeille', models.DateField()),
                ('statutStockCorbeille', models.CharField(choices=[('disponible', 'Disponible'), ('expire', 'Expire'), ('commande', 'Commande')], max_length=30)),
                ('DateDeCreationCorbeille', models.DateTimeField(auto_now_add=True)),
                ('dateSupressionStocks', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomFournisseur', models.CharField(max_length=50)),
                ('dateDeNaissanceFournisseur', models.DateField()),
                ('telephoneFournisseur', models.CharField(max_length=50)),
                ('adresseFournisseur', models.CharField(max_length=50)),
                ('DateDeCreation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stocks_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomStock', models.CharField(max_length=50)),
                ('quantiteStock', models.IntegerField()),
                ('DescriptionStock', models.CharField(max_length=200)),
                ('dateEntreeStock', models.DateField()),
                ('dateExpirationStock', models.DateField()),
                ('statutStock', models.CharField(choices=[('disponible', 'Disponible'), ('expire', 'Expire'), ('commande', 'Commande')], max_length=30)),
                ('DateDeCreation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produit_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomProduit', models.CharField(max_length=50)),
                ('categorieProduit', models.CharField(max_length=100)),
                ('prixProduit', models.FloatField()),
                ('descriptionProduit', models.CharField(max_length=200)),
                ('dateExpirationProduit', models.DateField()),
                ('DateDeCreation', models.DateTimeField(auto_now_add=True)),
                ('fournisseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produits', to='base.fournisseur_table')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produits', to='base.stocks_table')),
            ],
        ),
        migrations.CreateModel(
            name='Corbeille_Produits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomProduitCorbeille', models.CharField(max_length=50)),
                ('categorieProduitCorbeille', models.CharField(max_length=100)),
                ('prixProduitCorbeille', models.FloatField()),
                ('descriptionProduitCorbeille', models.CharField(max_length=200)),
                ('dateExpirationProduitCorbeille', models.DateField()),
                ('DateDeCreationCorbeille', models.DateTimeField(auto_now_add=True)),
                ('dateSupressionProduitsCorbeille', models.DateField(auto_now_add=True)),
                ('fournisseurCorbeille', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='corbeille_produits_fournisseur', to='base.fournisseur_table')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='corbeille_produits_stock', to='base.stocks_table')),
            ],
        ),
    ]
