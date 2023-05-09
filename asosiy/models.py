from django.db import models

<<<<<<< HEAD

class Aktyor(models.Model):
    ism = models.CharField(max_length=30)
    davlat = models.CharField(max_length=30, blank=True)
    tugilgan_yil = models.DateField()
    jins = models.CharField(max_length=7)
    def __str__(self):
        return self.ism

class Kino(models.Model):
    nom = models.CharField(max_length=50)
    janr = models.CharField(max_length=50)
    yil = models.DateField()
    aktyorlar = models.ManyToManyField(Aktyor)
=======
class Tarif(models.Model):
    nom = models.CharField(max_length=30)
    muddat = models.CharField(max_length=30)
    narx = models.PositiveSmallIntegerField()
>>>>>>> 740431b9d14d83c242d2a3e129979a09a529ca0e
    def __str__(self):
        return self.nom