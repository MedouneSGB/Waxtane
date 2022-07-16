from asyncio import SendfileNotAvailableError
from django.shortcuts import render, redirect
from .models import Sentence
from .form import SentenceForm

# Create your views here.
def view_index(request):
    data = Sentence.objects.all()

    return render(request, 'waxtane/index.html', {"data": data})

def view_form(request):
    forms = SentenceForm(request.POST)

    if forms.is_valid():
        forms.save() 

        return redirect('home')

    else:
        forms = SentenceForm()

    return render(request, 'waxtane/ajout.html', {'forms': forms})
    

