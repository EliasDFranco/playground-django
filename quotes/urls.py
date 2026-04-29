# URL  para la aplicación "quotes"
from django.urls  import path
from . import views
urlpatterns = [
    path("hola-mundo" , views.index),
    path("lunes", views.lunes),
    path("martes", views.martes),
]
