from django.contrib import admin
from django.core.exceptions import ValidationError
from datetime import date
from .models import Medecin, Patient, Consultation

@admin.register(Medecin)
class MedecinAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "nif", "date_naissance", "email")
    search_fields = ("nom", "prenom", "nif", "email")
    def save_model(self, request, obj, form, change):
        today = date.today()
        age = today.year - obj.date_naissance.year - ((today.month, today.day) < (obj.date_naissance.month, obj.date_naissance.day))
        if age < 26:
            raise ValidationError("Un médecin doit avoir au moins 26 ans.")
        super().save_model(request, obj, form, change)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "date_naissance", "telephone")
    search_fields = ("nom", "prenom", "telephone")

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ("patient", "medecin", "date_consultation", "description")
    search_fields = ("patient__nom", "medecin__nom")
    list_filter = ("date_consultation",)

