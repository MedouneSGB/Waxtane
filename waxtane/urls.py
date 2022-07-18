from django.urls import path
from . import views

# add urls
urlpatterns = [
    path("", views.view_nothing),
    path("home/", views.view_index, name='home'),
    path("ajout/", views.view_form, name='ajout')
]