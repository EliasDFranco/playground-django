from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.
def Home(request):
  today = date.today()
  return render(request,"landing/template.html", {
    "nombre": "Elias",
    "apellido": "Franco",
    "today": today,
  })
