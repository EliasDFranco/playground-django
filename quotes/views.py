from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def days_week_with_number(request, days):
  return HttpResponse(days)

def days_week(request, days):
  quoteText = None
  if days == "monday":
    quoteText = "Pienso, luego existo"
  
  elif days== "tuesday":
    quoteText = "Me chingué la rodilla "
  
  else: 
    return HttpResponseNotFound("No hay frase célebre para este día")
  
  return HttpResponse(quoteText)