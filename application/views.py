from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from application.models import medData

# Create your views here.
@login_required
def accueil(request):
	prenom = "ici le nom de l'utilisateur"
	return render(request, "accueil.html",
	       context={"prenom": prenom})

def visMedData(request):
	pourVisu = medData.objects.all()
	return render(request, "visMedData.html", locals())