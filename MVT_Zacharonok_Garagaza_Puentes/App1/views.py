from django.shortcuts import render
from django.http import HttpResponse
from App1.models import familiar

def monstrar_familiares(request):
  lista_familiares = familiar.objects.all()
  return render(request, "App1/familiares.html", {"lista_familiares": lista_familiares})
