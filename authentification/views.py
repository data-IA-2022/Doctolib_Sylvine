from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from authentification.models import Utilisateur
import random 
import string
import pandas as pd


def connexion(request):
    message = ""
    if request.method == "POST": # a-t-on reçu des data d'un formulaire ?
        username = request.POST["username"]
        motDePasse = request.POST["motDePasse"]
        verification = authenticate(username = username,
                                    password = motDePasse)
        if verification != None:
            login(request, verification)
            return redirect("accueil")
        else: # si la vérification n'est pas bonne
            message = "username ou/et mot de passe incorrect"
    return render(request,
                      "connexion.html", {"message" : message})

def deconnexion(request):
    logout(request)
    return redirect("connexion")

def inscription(request):
    ideeMDP = "".join([random.choice(string.printable) for _ in range(12)]).replace(" ", "")
    if request.method == "POST": # a-t-on reçu des data d'un formulaire ?
        username = request.POST["username"]
        motDePasse = request.POST["motDePasse"]
        nouveauCompte = Utilisateur.objects.create_user(username = username,
                                    password = motDePasse)
        return redirect("connexion")


    return render(request,
                    "inscription.html", {"ideeMDP" : ideeMDP.replace(" ", "")}) # ici, c'est s'il n'y a pas de requete post, ie on vient d'arriver sur la page pour la première fois


def alimentationPatients():
    listePatients = pd.read_csv("/home/sylvine/Documents/Projets/Projet10_Doctolib/Doctolib_Sylvine/authentification/data/listePatients.csv",
                                )
    for index, valeurs in listePatients.iterrows():
        Utilisateur.objects.create(username = valeurs.username,
                                   password = valeurs.motDePasse,
                                   role = "patient")
        
def alimentationMedecins():
    listeMedecins = pd.read_csv("/home/sylvine/Documents/Projets/Projet10_Doctolib/Doctolib_Sylvine/authentification/data/listeMedecins.csv",
                                )
    for index, valeurs in listeMedecins.iterrows():
        Utilisateur.objects.create(username = valeurs.username,
                                   password = valeurs.motDePasse,
                                   role = "medecin")
        
if len(Utilisateur.objects.filter(role="patient")) == 0:
    alimentationPatients()
if len(Utilisateur.objects.filter(role="medecin")) == 0:
    alimentationMedecins()
