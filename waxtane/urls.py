from django.urls import path
from . import views

# add urls
urlpatterns = [
    path("home/", views.view_index)
]