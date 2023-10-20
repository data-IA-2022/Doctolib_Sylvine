"""
URL configuration for doctolibbydjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from application.views import accueil, visMedData, comptes, edaia, associationMedecinPatient, create_med_data, tableVisualisation
from authentification.views import connexion, deconnexion, inscription

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accueil/",accueil, name = "accueil"), # le name est un alias pour retrouevr toutes les url via un chemin absolu
    path("",connexion, name ="connexion"),
    path("comptes", comptes, name="comptes"),
    path("deconnexion/",deconnexion, name="deconnexion"),
    path("inscription/",inscription, name="inscription"),
    path("visMedData/",visMedData, name="visMedData"),
    path("edaia/",edaia, name="edaia"),
    path("associationMedecinPatient/", associationMedecinPatient, name="associationMedecinPatient"),
    path("create_med_data/",create_med_data, name="create_med_data"),
    path("tableVisualisation/",tableVisualisation, name="tableVisualisation"),

]
