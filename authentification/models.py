from django.db import models
from django.contrib.auth.models import AbstractUser


class Utilisateur(AbstractUser):
    lesRoles = (
        ('patient', 'patient'),
        ("medecin", 'medecin'),
        ("responsable", "responsable"),
    )

    # Set the username field as the primary key
    username = models.CharField(
        verbose_name='Username',
        max_length=150,
        unique=True,
        primary_key=True  # This makes 'username' the primary key
    )

    role = models.CharField(max_length=30, 
                            choices=lesRoles, 
                            verbose_name='Rôle', null=True)


# à la main:
# class Connexion(models.Model):
#     username = models.CharField(max_length=50)
#     motDePasse = models.CharField(max_length=50)

class medecinPatient(models.Model):
    idPatient = models.ForeignKey(Utilisateur, 
                                  null=True, 
                                  on_delete=models.CASCADE,
                                   related_name='patientMedecin', 
                                   unique=True)
    idMedecin = models.ForeignKey(Utilisateur, 
                                  null=True, 
                                  on_delete=models.CASCADE,
                                   related_name='medecinPatient')