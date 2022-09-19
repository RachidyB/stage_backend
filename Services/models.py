
from django.db import models


class Technician(models.Model):
    id = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=255)
    Prenom = models.CharField(max_length=255)
    Profession = models.CharField(max_length=255)
    Date_Debut = models.DateField
    Telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.Nom


class Voiture(models.Model):
    Matricule = models.CharField(primary_key=True,max_length=20)
    Marque = models.CharField(max_length=50)
    Nombre_Cv = models.IntegerField()
    Serie = models.CharField(max_length=50)
    Annee= models.IntegerField()



    def __str__(self):
        return self.Marque


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    Technician = models.ForeignKey(Technician, on_delete=models.CASCADE)
    Voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE)
    Service_effectuée = models.CharField(max_length=255)
    Date_entrée = models.DateField()
    Date_sortie = models.DateField()

    def __str__(self):
        return str(self.Technician) + "- " + str(self.Voiture)
