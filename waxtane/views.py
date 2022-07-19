from django.shortcuts import render, redirect
from .models import Sentence
from .form import SentenceForm
from django.http import HttpResponse
import sqlite3
import pandas as pd
from django.db.models import Q

# Create your views here.

#La vue pour la page d'accueil
def view_index(request):
    #Les phrases de la barre de recherche 
    sentences = ""

    if 'q' in request.GET:
        q = request.GET['q']
        
        multiple_q = Q(Q(sentence_wolof__icontains=q) | Q(sentence_fr__icontains=q) | Q(sentence_en__icontains=q))
        sentences = Sentence.objects.filter(multiple_q)

    #Les phrases contenues dans le DB
    data = Sentence.objects.all()

    return render(request, 'waxtane/index.html', {"data": data, "sentences": sentences})

#La vue pour la pga e ajout
def view_form(request):
    #le code du formulaire lorsqu'une methode POST est passer 
    forms = SentenceForm(request.POST)

    if forms.is_valid():
        forms.save() 
        #Update data in file csv
        connexion_sql = sqlite3.connect("db.sqlite3")
        df = pd.read_sql_query("SELECT * from waxtane_sentence", connexion_sql)
        df.to_csv("data/waxtane.csv")

        return redirect('home')

    else:
        forms = SentenceForm()

    return render(request, 'waxtane/ajout.html', {'forms': forms})

#Une fonction permettant de retourner les visiteurs vers la page d'accueil lorsque le route qu'ils ont taper est vide 
def view_nothing(request):
    return redirect("home")
    

