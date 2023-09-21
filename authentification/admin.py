from django.contrib import admin
from authentification.models import Utilisateur, medecinPatient


class colonnes(admin.ModelAdmin):
    list_display = ("username","role","email","is_superuser",)
    # search_fields = ["username","role","email","is_superuser",]
    search_fields = [field.name for field in Utilisateur._meta._get_fields()]

admin.site.register(Utilisateur)

admin.site.register(medecinPatient)