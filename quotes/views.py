from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  return HttpResponse("Hola mundo desde Django")

def lunes(request):
  return HttpResponse("Esto es un dia lunes")

def martes(request):
  return HttpResponse("Eso de alla es Martes")