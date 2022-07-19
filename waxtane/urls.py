from django.urls import path
from . import views

# les Routes de l'application web
urlpatterns = [
    path("", views.view_nothing),
    path("home/", views.view_index, name='home'),
    path("ajout/", views.view_form, name='ajout')
]