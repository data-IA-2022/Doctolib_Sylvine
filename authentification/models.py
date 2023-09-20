from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    pass


# à la main:
# class Connexion(models.Model):
#     username = models.CharField(max_length=50)
#     motDePasse = models.CharField(max_length=50)