# flight_app/models.py

from django.db import models

class Compagnie(models.Model):
    nom = models.CharField(max_length=100)
    ville = models.ForeignKey('Ville', on_delete=models.CASCADE)
    uuid = models.UUIDField()

class Ville(models.Model):
    nom = models.CharField(max_length=100)
    pays = models.ForeignKey('Pays', on_delete=models.CASCADE)

class Pays(models.Model):
    nom = models.CharField(max_length=100)

class Vol(models.Model):
    compagnie = models.ForeignKey(Compagnie, on_delete=models.CASCADE)
    date_depart = models.DateTimeField()
    date_arrivee = models.DateTimeField()
    ville_depart = models.ForeignKey(Ville, related_name='depart', on_delete=models.CASCADE)
    ville_arrivee = models.ForeignKey(Ville, related_name='arrivee', on_delete=models.CASCADE)
    prix_adulte = models.DecimalField(max_digits=10, decimal_places=2)
    prix_enfant = models.DecimalField(max_digits=10, decimal_places=2)
    prix_bebe = models.DecimalField(max_digits=10, decimal_places=2)
    prix_allee_simple = models.DecimalField(max_digits=10, decimal_places=2)
    prix_allee_retour = models.DecimalField(max_digits=10, decimal_places=2)

class MonVol(models.Model):
    vol = models.ForeignKey(Vol, on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    nbre_adulte = models.IntegerField()
    nbre_bebe = models.IntegerField()
    nbre_enfant = models.IntegerField()
    uuid = models.UUIDField()

class User(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    # Autres champs utilisateur

class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)

class Payment(models.Model):
    mon_vol = models.ForeignKey(MonVol, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    mode_payment = models.CharField(max_length=20)  # cash ou mobile
    uuid = models.UUIDField()
