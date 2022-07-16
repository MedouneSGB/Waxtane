from django.db import models

# Create your models here.
class Sentence(models.Model):

    #le champ pour la langue wolof
    sentence_wolof = models.TextField()
    #le champ pour la langue francaise
    sentence_fr = models.TextField()
    #le champ pour la langue anglaise
    sentence_en = models.TextField()
