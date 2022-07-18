#importer les modules
from django.test import TestCase
from .models import Sentence

#Creation des cas de testes 
class Test_data(TestCase):
    #Une fonction permettant de faire des testes sur les modeles
    def test_sentences(self):
        sentences = Sentence()
        sentences.sentence_wolof = "teste 1"
        sentences.sentence_fr = "teste 2"
        sentences.sentence_en = "teste 3"


        self.assertEqual( sentences.sentence_wolof, "teste 1")
        self.assertEqual( sentences.sentence_fr, "teste 2")
        self.assertEqual( sentences.sentence_en, "teste 3")
