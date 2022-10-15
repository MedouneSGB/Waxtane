import requests
import json
import csv
from pprint import pprint
from bs4 import BeautifulSoup
from googletrans import Translator

url = 'https://jangawolof.org/phrases/'
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
figures = soup.find_all("figure", class_='wp-block-table')
selectedFigures = figures[2:]
phrases = []
englishPhrases = []
wolofPhrases = []
frenchPhrases = []
for figure in selectedFigures:
    listOfElt = figure.find_all('td')
    for elt in listOfElt:
        phrases.append(elt.text.replace(u'\xa0', u' '))

for index, phrase in enumerate(phrases):
    if index % 2 == 0:
        englishPhrases.append(phrase)
    else:
        wolofPhrases.append(phrase)

numberOf = 62
for index, phrase in enumerate(englishPhrases):
    translator = Translator()
    print(f'> Traduction de la phrase n°{index}')
    translation = translator.translate(phrase, src='en', dest='fr')
    frenchPhrases.append(translation.text)
    data = [numberOf + 1, wolofPhrases[index], translation.text, phrase]
    print(f'> Couple de phrase généré: {data}')
    f = open('countries.csv', 'a', encoding='UTF8', newline='\n')
    writer = csv.writer(f)
    writer.writerow(data)
    f.close()
    print(
        f'> Fin du process pour la phrase n°{index} <')
    numberOf = numberOf + 1
