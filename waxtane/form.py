from django.forms import ModelForm
from .models import Sentence

#Mode de formulaire pour le modele sentence
class SentenceForm(ModelForm):
    class Meta:
        model = Sentence
        fields = ["sentence_wolof", "sentence_fr", "sentence_en"]
