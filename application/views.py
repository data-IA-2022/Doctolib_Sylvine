from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from application.models import medData
from django.contrib.auth import authenticate
from authentification.models import Utilisateur, medecinPatient
import pandas as pd
import csv
import numpy as np
from application.forms import MedDataForm
import datetime


@login_required
# page d'accueil
def accueil(request):
    prenom = request.user.username
    return render(request,"accueil.html",
                  context={"prenom": prenom})

@login_required
# page visualisation des données
def visMedData(request): # version Sylvine
	pourVisu = medData.objects.all()
	return render(request, "visMedData.html", locals())

@login_required
def tableVisualisation(request): # version Patrick
    if request.user.role not in ["responsable","patient","medecin"]:
        return redirect("accueil")
    
    else: 
        user = request.user.username
        # On récupère le nom des champs de la table medData
        champsMedData = [field.name for field in medData._meta.get_fields()]

        if request.user.role == "responsable":
            # on récupère une liste de tous les id contenus dans la table medData
            idMedData = [valeur.id for valeur in medData.objects.all()]
            # pour chaque id récupéré, on extrait de la table les valeurs dans le premier (et unique ici) élément du dictionnaire correpsondant à l'id
            dataMedData = [medData.objects.filter(id=id).values()[0].values() for id in idMedData]

        elif request.user.role == "patient":
            #collect all lines for this user
            dataMedData_user = medData.objects.filter(anonymousID=user).values() # this returns a list of dictionnaries, one dic for each line of medData for this user
            # for each dictionnary (i in range length of the dictionnary), get the values
            dataMedData = [dataMedData_user.values()[i].values() for i in range(dataMedData_user.count())]
        
        elif request.user.role == "medecin":
            # if médecin
            # Query the medecinPatient model to get all idPatient instances corresponding to the idMedecin
            idPatients_list = medecinPatient.objects.filter(idMedecin__username=user).values_list('idPatient', flat=True)
            # filter the medData table on all idPatient retrieved in the list
            dataMedData_user = medData.objects.filter(anonymousID__in=idPatients_list).values()
            # for each dictionnary (i in range length of the dictionnary), get the values
            dataMedData = [dataMedData_user.values()[i].values() for i in range(dataMedData_user.count())]

        return render(request, "tableVisualisation.html",
                {"dataMedData" : dataMedData,
                "champsMedData" : champsMedData,
                "user" : user})




@login_required
# réinitialisation mdp
def comptes(request):
    regexMDP = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+-]).{8,}$"
    message = ""
    if request.method == "POST":
        ancienMDP = request.POST["ancienMDP"]
        nouveauMDP1 = request.POST["nouveauMDP1"]
        nouveauMDP2 = request.POST["nouveauMDP2"]
        
        verification = authenticate(username = request.user.username,
                                    password = ancienMDP)
        if verification != None:
            if nouveauMDP1 == nouveauMDP2:
                utilisateur = Utilisateur.objects.get(username = request.user.username)
                #utilisateur = Utilisateur.objects.get(id=request.user.id)
                utilisateur.set_password(request.POST.get("nouveauMDP1"))
                utilisateur.save()
                return redirect("accueil")
            else:
                message = "⚠️ Les deux mot de passe ne concordent pas ⚠️"
        else:
            message = "L'ancien mot de passe n'est pas bon. T'es qui toi ? 😡"
    return render(request,
                  "comptes.html",
                  {"regexMDP" : regexMDP, "message" : message})

@login_required
# page avec eda et ia pour uniquement le médecin
def edaia(request):
    if request.user.role != "medecin":
        return redirect("accueil")
    else:
        return render(request, "edaia.html")

@login_required
def associationMedecinPatient(request):
    # 1- Récupérer la liste des id des médecins et des patients
    # 2- Ensuite on ne garde que les patients qui ne sont pas dans la table medecinPatient
    # 3- On créé ensuite un template qui contiendra une liste déroulante
    # 4- Dans cette liste déroulante on va afficher d'un côté les médecins
    # et de l'autre les patients filtrés (voir étape 2)
    # https://developer.mozilla.org/fr/docs/Web/HTML/Element/select
    
    medecins = [medecin for medecin in Utilisateur.objects.filter(role="medecin")]
    patients = [patient for patient in Utilisateur.objects.filter(role="patient")]
    listePatientsAssocies = [ligne.idPatient for ligne in medecinPatient.objects.all()]
    print("listePatientsAssocies :", listePatientsAssocies)
    listePatientsNonAssocies = [patient for patient in patients if patient not in listePatientsAssocies]
    tableAssociationMedecinPatient = medecinPatient.objects.all()
    
    if request.method == "POST":
        medecin = request.POST["medecin"]
        patient = request.POST["patient"]
        print("medecin", type(medecin), medecin)
        medecinPatient(idMedecin = Utilisateur.objects.filter(username=medecin)[0], 
                       idPatient = Utilisateur.objects.filter(username=patient)[0]).save()
        return redirect("associationMedecinPatient")
    return render(request, "associationMedecinPatient.html",
                  {"listePatientsNonAssocies" : listePatientsNonAssocies,
                   "medecins" : medecins,
                   "tableAssociationMedecinPatient" : tableAssociationMedecinPatient})


# alimenter BDD medData
def alimentationMedData():  
    donnees = pd.read_csv("/home/sylvine/Documents/Projets/Projet10.2_Doct/Doctolib_Sylvine/application/data/dataMed.csv")
    donnees = donnees.replace(np.nan, None)

    for index, row in donnees.iterrows():
        patient_username_str = row['AnonymousID']
        # ligne = Utilisateur.objects.filter(username=patient_username_str).values()[0].values()
        # patient_username = list(ligne)[0]

        # il faut que le nom type 'P01' soit une instance et pas une string
        utilisateur_instance, created = Utilisateur.objects.get_or_create(username=patient_username_str)

        medData.objects.create(
            anonymousID=utilisateur_instance,
            date=row['Date'],
            poids=row['Poids'],
            tourTaille=row['tourTaille'],
            freqCard=row['FreqCard'],
            systMatin=row['SystoMatin'],
            systSoir=row['SystoSoir'],
            diastMatin=row['DiastMatin'],
            diastSoir=row['DiastSoir'],
            symptCardio=row['SymptCardio'],
            nbMed=row['NbMed'],
            oubliMatinYN=row['OubliMatinYN'] == 'y',  # CoMedDataForm
            symptomesYN=row['SymptomesYN'] == 'y',
            effetSympt=row['EffetSympt'],
            alcoolYN=row['AlcoolYN'] == 'y',
            grignoSucreYN=row['GrignoSucreYN'] == 'y',
            grignoSaleYN=row['GrignoSaleYN'] == 'y',
            nbRepas=row['NbRepas'],
            qqteEau=row['QqteEau'],
            qqteAlcool=row['QqteAlcool'],
            actPhysYN=row['ActPhysYN'] == 'y',
            actPhys=row['ActPhys'],
            dureeActPhys=row['DureeActPhys'],
            dyspneeYN=row['DyspneeYN'] == 'y',
            oedemeYN=row['OedemeYN'] == 'y',
            infectionYN=row['InfectionYN'] == 'y',
            fievreYN=row['FievreYN'] == 'y',
            palpitationYN=row['PalpitationYN'] == 'y',
            douleurThoYN=row['DouleurThoYN'] == 'y',
            malaiseYN=row['MalaiseYN'] == 'y',
            debutPalp=row['DebutPalp'],
            durationPalp=row['DurationPalp'],
            debutDouleurTho=row['DebutDouleurTho'],
            durationDouleurTho=row['DurationDouleurTho'],
            debutMalaise=row['DebutMalaise'],
            durationMalaise=row['DurationMalaise'],
            irritab=row['Irritab'],
            depression=row['Depression'],
            boucheSeche=row['BoucheSeche'],
            gestesImpulsifs=row['GestesImpulsifs'],
            grincementDents=row['GrincementDents'],
            difficulteAssis=row['DifficulteAssis'],
            cauchemars=row['Cauchemars'],
            diarrhee=row['Diarrhee'],
            attaqueVerb=row['AttaqueVerb'],
            hautBasEmot=row['HautBasEmot'],
            enviePleurer=row['EnviePleurer'],
            envieFuir=row['EnvieFuir'],
            envieFaireMal=row['EnvieFaireMal'],
            penseeEmbr=row['PenseeEmbr'],
            debitRapide=row['DebitRapide'],
            fatigue=row['Fatigue'],
            sentimentSurcharge=row['SentimentSurcharge'],
            sentimentFragile=row['SentimentFragile'],
            sentimentTristesse=row['SentimentTristesse'],
            sentimentAnxiete=row['SentimentAnxiete'],
            tensionEmot=row['TensionEmot'],
            hostilite=row['Hostilite'],
            tremblements=row['Tremblements'],
            begaiements=row['Begaiements'],
            diffConcentrer=row['DiffConcentrer'],
            diffPensee=row['DiffPensee'],
            diffDormir=row['DiffDormir'],
            besoinUriner=row['BesoinUriner'],
            mauxEstomac=row['MauxEstomac'],
            impatience=row['Impatience'],
            mauxTete=row['MauxTete'],
            douleurDos=row['DouleurDos'],
            appetit=row['Appetit'],
            sexe=row['Sexe'],
            oublis=row['Oublis'],
            douleurPoitrine=row['DouleurPoitrine'],
            conflits=row['Conflits'],
            diffLever=row['DiffLever'],
            sentimentHorsCtrl=row['SentimentHorsCtrl'],
            diffActivite=row['DiffActivite'],
            retrait=row['Retrait'],
            diffEndormir=row['DiffEndormir'],
            diffRemettreEvent=row['DiffRemettreEvent'],
            mainsMoites=row['MainsMoites']
        )

# aliment only if table is empty
if medData.objects.count() == 0:
    alimentationMedData()

@login_required
def create_med_data(request):
    user = request.user.username
    dateJour = datetime.datetime.now()
    form = MedDataForm()

    if request.method == 'POST':
        form = MedDataForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'form_success.html', {'message': 'Formulaire soumis avec succès!'})

    context = {
        'form': form,
        'user': user
    }

    return render(request, 'form.html', context)


def rgpd(request):
    return render(request,"rgpd.html",
                context={"site_name": "Bee Patient"})