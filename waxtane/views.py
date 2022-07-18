from django.shortcuts import render, redirect
from .models import Sentence
from .form import SentenceForm
import sqlite3
import pandas as pd

# Create your views here.
def view_index(request):
    data = Sentence.objects.all()

    return render(request, 'waxtane/index.html', {"data": data})

def view_form(request):
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


def view_nothing(request):
    return redirect("home")
    

