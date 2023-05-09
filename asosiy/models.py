from django.db import models

class Tarif(models.Model):
    nom = models.CharField(max_length=30)
    muddat = models.CharField(max_length=30)
    narx = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.nom