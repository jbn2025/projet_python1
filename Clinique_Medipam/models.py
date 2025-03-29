from django.db import models
from django.core.exceptions import ValidationError
from datetime import date





def validate_age(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 26:
        raise ValidationError("Le Medecin doit avoir au moins 26 ans.")

class Medecin(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    nif = models.CharField(max_length=20, unique=True)
    date_naissance = models.DateField(validators=[validate_age])  # Ajout de la validation
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Patient(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    telephone = models.CharField(max_length=15, unique=True)
    photo = models.ImageField(upload_to="static/images/patients_photos/", blank=True, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Consultation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="consultations")
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE, related_name="consultations")
    date_consultation = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return f"Consultation de {self.patient} par {self.medecin} - {self.date_consultation}"
