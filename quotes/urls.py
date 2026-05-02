# URL  para la aplicación "quotes"
from django.urls  import path
from . import views
urlpatterns = [
    path("<days>", views.days_week),
]
