from django.db import models


class medData(models.Model):
    YesNoChoices =[
        ("y", "Yes"),
        ("n", "No")
    ]
 
    anonymousID = models.CharField(max_length=50) # trouver moyen pour remplir auto avec l'ID avec la table correspondance avec username
    date = models.DateField(auto_now=True) 
    poids = models.DecimalField(max_digits=6, decimal_places=2)
    freqCard = models.IntegerField()
    systMatin = models.IntegerField()
    systSoir = models.IntegerField()
    diastMatin = models.IntegerField()
    diastSoir = models.IntegerField()
    symptCardio = models.CharField(max_length=100, null=True)
    nbMed = models.IntegerField()
    oubliMatinYN = models.BooleanField(default=False) #
    oubliSoirYN = models.BooleanField(default=False)  #
    effetSecYN = models.BooleanField(default=False) #
    symptomesYN = models.BooleanField(default=False) #
    effetSympt = models.CharField(max_length=100,null=True)
    alcoolYN = models.BooleanField(default=False) #
    grignoSucreYN = models.BooleanField(default=False) #
    grignoSaleYN = models.BooleanField(default=False) #
    nbRepas = models.IntegerField()
    qqteEau = models.DecimalField(max_digits=6, decimal_places=2)
    qqteAlcool = models.DecimalField(max_digits=6, decimal_places=2)
    actPhysYN = models.BooleanField(default=False) #
    actPhys = models.CharField(max_length=100,null=True)
    dureeActPhys = models.IntegerField(null=True)
    dyspneeYN = models.BooleanField(default=False) #
    oedemeYN = models.BooleanField(default=False) #
    infectionYN = models.BooleanField(default=False) #
    fievreYN = models.BooleanField(default=False) #
    palpitationYN = models.BooleanField(default=False) #
    douleurThoYN = models.BooleanField(default=False) #
    malaiseYN = models.BooleanField(default=False) #
    debutPalp = models.TimeField(null=True)
    durationPalp = models.DurationField(null=True)
    debutDouleurTho = models.TimeField(null=True)
    durationDouleurTho = models.DurationField(null=True)
    debutMalaise = models.TimeField(null=True)
    durationMalaise = models.DurationField(null=True)

    stressChoices = (
        (0, "0"),
        (1, "1"),
        (5, "5"),
        (10, "10"),
    )

    irritab = models.IntegerField(default =0, choices=stressChoices)
    depression = models.IntegerField(default =0, choices=stressChoices)
    boucheSeche = models.IntegerField(default =0, choices=stressChoices)
    gestesImpulsifs = models.IntegerField(default =0, choices=stressChoices)
    grincementDents = models.IntegerField(default =0, choices=stressChoices)
    difficulteAssis = models.IntegerField(default =0, choices=stressChoices)
    cauchemars = models.IntegerField(default =0, choices=stressChoices)
    diarrhee = models.IntegerField(default =0, choices=stressChoices)
    attaqueVerb = models.IntegerField(default =0, choices=stressChoices)
    hautBasEmot = models.IntegerField(default =0, choices=stressChoices)
    enviePleurer = models.IntegerField(default =0, choices=stressChoices)
    envieFuir = models.IntegerField(default =0, choices=stressChoices)
    envieFaireMal = models.IntegerField(default =0, choices=stressChoices)
    penseeEmbr = models.IntegerField(default =0, choices=stressChoices)
    debitRapide = models.IntegerField(default =0, choices=stressChoices)
    fatigue = models.IntegerField(default =0, choices=stressChoices)
    sentimentSurcharge = models.IntegerField(default =0, choices=stressChoices)
    sentimentFragile = models.IntegerField(default =0, choices=stressChoices)
    sentimentTristesse = models.IntegerField(default =0, choices=stressChoices)
    sentimentAnxiete = models.IntegerField(default =0, choices=stressChoices)
    tensionEmot = models.IntegerField(default =0, choices=stressChoices)
    hostilite = models.IntegerField(default =0, choices=stressChoices)
    tremblements = models.IntegerField(default =0, choices=stressChoices)
    begaiements = models.IntegerField(default =0, choices=stressChoices)
    diffConcentrer = models.IntegerField(default =0, choices=stressChoices)
    diffPensee = models.IntegerField(default =0, choices=stressChoices)
    diffDormir = models.IntegerField(default =0, choices=stressChoices)
    besoinUriner = models.IntegerField(default =0, choices=stressChoices)
    mauxEstomac = models.IntegerField(default =0, choices=stressChoices)
    impatience = models.IntegerField(default =0, choices=stressChoices)
    mauxTete = models.IntegerField(default =0, choices=stressChoices)
    douleurDos = models.IntegerField(default =0, choices=stressChoices)
    appetit = models.IntegerField(default =0, choices=stressChoices)
    sexe = models.IntegerField(default =0, choices=stressChoices)
    oublis = models.IntegerField(default =0, choices=stressChoices)
    douleurPoitrine = models.IntegerField(default =0, choices=stressChoices)
    conflits = models.IntegerField(default =0, choices=stressChoices)
    diffLever = models.IntegerField(default =0, choices=stressChoices)
    sentimentHorsCtrl = models.IntegerField(default =0, choices=stressChoices)
    diffActivite = models.IntegerField(default =0, choices=stressChoices)
    retrait = models.IntegerField(default =0, choices=stressChoices)
    diffEndormir = models.IntegerField(default =0, choices=stressChoices)
    diffRemettreEvent = models.IntegerField(default =0, choices=stressChoices)
    mainsMoites = models.IntegerField(default =0, choices=stressChoices)
    #totalStress = models.Sum() #???



