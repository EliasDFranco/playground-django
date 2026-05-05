from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
days_of_week = {
  "monday": "Pienso luego existo",
  "tuesday": "Me chingué la rodilla",
  "wednesday": "Ay caramba",
  "thursday": "Hoy toca porque toca",
  "friday": "Vamonos al after office",
  "saturday": "En el séptimo día descanso",
  "sunday": "Hoy se come asado",
}

def days_week_with_number(request, day):
    days = list(days_of_week.keys())
    if day > len(days):
        return HttpResponseNotFound("Este día no existe")
    redirect_day = days[day - 1]
    return HttpResponseRedirect(f"/quotes/{redirect_day}")

def days_week(request, day):
    try:
        quoteText = days_of_week[days]
        return HttpResponse(quoteText)
    except:
        return HttpResponseNotFound("Error: Esto no es un día de la semana")
  