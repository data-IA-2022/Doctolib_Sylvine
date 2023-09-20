# Generated by Django 4.2.5 on 2023-09-19 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("application", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="meddata",
            name="appetit",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="attaqueVerb",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="begaiements",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="besoinUriner",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="boucheSeche",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="cauchemars",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="conflits",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="debitRapide",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="depression",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="diarrhee",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="diffActivite",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="diffConcentrer",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="diffDormir",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="diffEndormir",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="diffLever",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="diffPensee",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="diffRemettreEvent",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="difficulteAssis",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="douleurDos",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="douleurPoitrine",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="envieFaireMal",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="envieFuir",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="enviePleurer",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="fatigue",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="gestesImpulsifs",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="grincementDents",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="hautBasEmot",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="hostilite",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="impatience",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="irritab",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="mainsMoites",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="mauxEstomac",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="mauxTete",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="oublis",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="penseeEmbr",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="retrait",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="sentimentAnxiete",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="sentimentFragile",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="sentimentHorsCtrl",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="sentimentSurcharge",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="sentimentTristesse",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="sexe",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="tensionEmot",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
        migrations.AddField(
            model_name="meddata",
            name="tremblements",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (5, "5"), (10, "10")], default=0
            ),
        ),
    ]
