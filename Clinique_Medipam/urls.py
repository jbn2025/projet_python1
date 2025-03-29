from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('admin/')),
    path('', lambda request: redirect('admin/')),  # Redirection automatique vers l'admin
    
]
