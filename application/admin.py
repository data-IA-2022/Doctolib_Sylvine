from django.contrib import admin
from authentification.models import Utilisateur
from application.models import medData


admin.site.register(medData)
admin.site.register(Utilisateur)

