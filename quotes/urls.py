# URL  para la aplicación "quotes"
from django.urls  import path, include
from . import views
urlpatterns = [
    path("hola-mundo" , views.index),
]
