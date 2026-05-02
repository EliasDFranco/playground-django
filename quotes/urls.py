# URL  para la aplicación "quotes"
from django.urls  import path
from . import views
urlpatterns = [
    path("<int:days>", views.days_week_with_number),
    path("<str:days>", views.days_week),
]
