# Generated by Django 4.2.5 on 2023-11-15 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="medData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                (
                    "poids",
                    models.DecimalField(decimal_places=2, max_digits=6, null=True),
                ),
                ("tourTaille", models.DecimalField(decimal_places=2, max_digits=6)),
                ("freqCard", models.IntegerField()),
                ("systMatin", models.IntegerField()),
                ("systSoir", models.IntegerField()),
                ("diastMatin", models.IntegerField()),
                ("diastSoir", models.IntegerField()),
                (
                    "symptCardio",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("nbMed", models.IntegerField()),
                ("oubliMatinYN", models.BooleanField(default=False)),
                ("oubliSoirYN", models.BooleanField(default=False)),
                ("effetSecYN", models.BooleanField(default=False)),
                ("symptomesYN", models.BooleanField(default=False)),
                ("effetSympt", models.CharField(blank=True, max_length=100, null=True)),
                ("alcoolYN", models.BooleanField(default=False)),
                ("grignoSucreYN", models.BooleanField(default=False)),
                ("grignoSaleYN", models.BooleanField(default=False)),
                ("nbRepas", models.IntegerField()),
                ("qqteEau", models.DecimalField(decimal_places=2, max_digits=6)),
                ("qqteAlcool", models.DecimalField(decimal_places=2, max_digits=6)),
                ("actPhysYN", models.BooleanField(default=False)),
                ("actPhys", models.CharField(blank=True, max_length=100, null=True)),
                ("dureeActPhys", models.IntegerField(blank=True, null=True)),
                ("dyspneeYN", models.BooleanField(default=False)),
                ("oedemeYN", models.BooleanField(default=False)),
                ("infectionYN", models.BooleanField(default=False)),
                ("fievreYN", models.BooleanField(default=False)),
                ("palpitationYN", models.BooleanField(default=False)),
                ("douleurThoYN", models.BooleanField(default=False)),
                ("malaiseYN", models.BooleanField(default=False)),
                ("debutPalp", models.TimeField(blank=True, null=True)),
                ("durationPalp", models.IntegerField(blank=True, null=True)),
                ("debutDouleurTho", models.TimeField(blank=True, null=True)),
                ("durationDouleurTho", models.IntegerField(blank=True, null=True)),
                ("debutMalaise", models.TimeField(blank=True, null=True)),
                ("durationMalaise", models.IntegerField(blank=True, null=True)),
                (
                    "irritab",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "depression",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "boucheSeche",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "gestesImpulsifs",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "grincementDents",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "difficulteAssis",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "cauchemars",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "diarrhee",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "attaqueVerb",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "hautBasEmot",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "enviePleurer",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "envieFuir",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "envieFaireMal",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "penseeEmbr",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "debitRapide",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "fatigue",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "sentimentSurcharge",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "sentimentFragile",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "sentimentTristesse",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "sentimentAnxiete",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "tensionEmot",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "hostilite",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "tremblements",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "begaiements",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "diffConcentrer",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "diffPensee",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "diffDormir",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "besoinUriner",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "mauxEstomac",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "impatience",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "mauxTete",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "douleurDos",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "appetit",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "sexe",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "oublis",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "douleurPoitrine",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "conflits",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "diffLever",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "sentimentHorsCtrl",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "diffActivite",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "retrait",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "diffEndormir",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "diffRemettreEvent",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "mainsMoites",
                    models.IntegerField(
                        choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
                    ),
                ),
                (
                    "anonymousID",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
