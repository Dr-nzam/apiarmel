from django.db import models

# Create your models here.


class Produit (models.Model):
    
    nom = models.CharField(max_length=128)
    
    description = models.TextField()
    
    prix = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.nom
    
    