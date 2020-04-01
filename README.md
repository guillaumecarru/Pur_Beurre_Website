# Site Pur Beurre

Ce site répond aux attentes de la startup Pur Beurre, qui souhaite développer une plateforme pour ses clients.
Il permettra de trouver un substitut sain à un aliment.
Pour se faire, il se servira de la base de données OpenFoodFacts.

## Description

1. **Python**
Python 3.6 est utilisé pour ce projet. N'ayant pas essayé d'autres versions, merci de me laisser un commentaire en issue si vous rencontrez des problèmes.

2. **tests écrits à la fin d’une fonctionnalité**
Pour chaque fonctionnalité ajoutée, des tests unitaires ont été effectués pour s'assurer de la qualité du code et de pouvoir répondre aux besoins du projet.
**Coverage est utilisé en parallèle avec les tests de django. Ils sont utilisables seulement en mode développement.**

3. **Django**
Django permet de partitionner les différentes parties du site en applications.
Cela permet d'utiliser une méthode de travail itérative, d'implémenter une fonctionnalité après l'autre.

4. **Heroku**
Du coté serveur, on se sert de la paas (plateform as a server) Heroku.
Le serveur en lui même est gunicorn.

5. **Postgresql**
Afin d'optimiser l'expérience, Heroku offre à ses utilisateurs une quantité de stockage de données avec PostgreSQL de 10 000 valeurs.

## Installation

1. **En local**
*Installer pipenv
*Cloner le repo master sur votre marchine.

Pour faire des tests unitaires:
* pipenv shell
* python manage.py runserver (dans la racine du projet)

Pour lancer le site en local:
* Créer un fichier .env à la racine du projet définissant les varibles d'environnement ou BDD correspondra au nom de votre base de données postgresql, USER le nom d'utilisateur de la base, PW_POSTGRES le mot de passe de l'utilisateur, et KEY_PROD la clé de production.
* python manage.py migrate (Création de la base de données)
* python manage.py populate_db (Peuplement de la base de données)
* Vous n'aurez ensuite qu'à lancer la commande **python manage.py runserver**.

2. **Par Heroku**
* Utiliser le repo prod
* Se logger sur git
* Se logger sur Heroku : heroku login
* Entrer le nom d'une variable d'environnement de clé : heroku config:set KEY_PROD=’nomdelacle’
* Création de la bdd postgreSQL : heroku addons:create heroku-postgresql:hobby-dev
* Enfin faire un push : git push heroku prod:master

## Applications

Vous trouverez dans **dbproducts** toutes les informations relatives à la base de données, et traitement de ces dernières.
Les informations relatives aux utilisateurs, création et gestion de comptes se trouvent dans **users**.
La page principale, le template de base, et les static se trouvent dans **main**.
La gestion des favoris se trouve dans l'application **favorites**.

## Informations diverses
Pour toute information concernant ce projet, veuillez me contacter par mail.
