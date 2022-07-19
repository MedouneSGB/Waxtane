# Contribuer au projet

Pour travailler sur ce projet vous devez en premier installer :

``python (3.10+)`` et ``pip``

Et suivre les étapes suivantes

#### 1 - Créer un environnement virtuel

Windows

```$ py -m venv waxtane_project```

Linux

```$ python3 -m venv waxtane_project```

Changer de répetoire

```$ cd waxtane_project```

#### 2 - Activer l'environnement

Windows

```$ Scripts\activate```

Linux

```$ source bin/activate```

#### 3 - Installation du projet

```bash
$ git clone -b python_version https://github.com/MedouneSGB/Waxtane.git 

$ cd Waxtane
```

#### 4 - Installation des dépendances

Windows

``$ pip install -r requirements.txt``

Linux

```bash
# Installer le package wheel
$ pip3 install wheel

# Installer les dependances
$ pip3 install -r requirements.txt
```

#### 5 - Executer le serveur

Windows

```$ py manage.py runserver```

Linux

```$ python3 manage.py runserver```

Dans votre navigateur tapez : ``localhost:8000``

#### Routes

Routes | Utilités
-------| -----------------------------------
home/  | Page d'accueil
ajout/ | Page pour ajouter des prhrases

#### Dossiers importants

Dossiers       | Utilités
---------------|------------------------------------
server         | Serveur de l'application web
waxtane        | L'application web
