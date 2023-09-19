from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def accueil(request):
	prenom = "Coco l'asticot"
	return render(request, "accueil.html",
	       context={"prenom": prenom})
