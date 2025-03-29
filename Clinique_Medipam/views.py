from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Medecin, Patient, Consultation
from django.db.models import Count
def index(request):
    return render(request, 'index.html')








