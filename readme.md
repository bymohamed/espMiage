
# Lucioles Temperatures Management System

![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)  
Par BEN YAMNA Mohamed et KHALIFA Hassen

Le projet «**Lucioles Temperatures Management System**» vise à construire des outils de supervision de la température pour les salles du bâtiments Lucioles (et la luminosité dans un deuxième point).

Grand merci à l'architecte Ahmed Ksiksi pour le refait du plan du bâtiment.

![plan](https://filebin.net/yxde4wfyn9o3ymum/BENY_00001.svg?t=hsee8o17)
## Pour commencer

Pour télécharger il suffit de lancer cette commande dans votre terminal

    $ git clone https://github.com/bymohamed/espMiage.git

### Pré-requis

Les pré-requis sont indiqués dans le fichier *requirements.txt*
La méthode d'installation est expliquée ci-dessous dans la partie **Installation**

 1. asgiref 3.3.1 
 2. Django 3.1.6 
 3. paho-mqtt 1.5.1 
 4. pytz 2021.1 
 5. sqlparse 0.4.1

### Installation
Après avoir télécharger le répo il suffit de suivre ces étapes : 

 - Créer un environnement virtuel
 - Activer l'environnement virtuel
 - Installer les dépendences
 - Compiler et excuter le code


```
$ virtualenv env
```
```
$ source env/bin/activate
```
```
$ pip install -r requirements.txt
```
```
$ cd project_dashboard
```
```
$ python manage.py runserver
```
Vous pouvez accéder au projet sous le lien http://localhost:8000/
## Démarrage

La Landing Page est le page de connexion ( root:Admin ).
![Login page](https://i2.paste.pics/72f6955cc4ee8962a4f4922881199b15.png) 
Une fois connecté vous serez rédigé vers la page du dashboard.

![dashboard](https://i2.paste.pics/53b564e8a1fb0ef720bcaed77d737212.png)
La dashboard contient uniquement un tableau de données collecté du MQTT pour le moment.



## Versions
Liste des versions ici 

**version  :** 0.1
C'est la première version sans front.
La communication se fait à l'aide des requetes GET envoyées par la carte ESP32 sur un lien de site qui recoie ses requetes consituté de 2 arguments : 
Arg 1 : Valeur de la temperature (exemple **25,60**)
Arg 2 : Nom de la carte entré en dur dans le code de l'ESP32 (exemple **ESP1**)

Les valeurs seront stockés dans une base de données SQLITE avec une 3eme colonne qui indique la date et l'heure de l'ajout de cette valeur.

Cette version comporte aussi un interface login. (root:Admin)

**Dernière version :** 0.2
Nous avons basculé dans la deuxième version sur un autre système que les requêtes GET. Nous utilisons un serveur MQTT pour l'échange de données.

Nous avons aussi ajouter un interface front-end et une page d'administration.

## A implimenter

 - Chiffrement des échanges.
 - Signature des échanges et vérifications.
 - ChartJs pour une meilleure présentation du données.
 - Mapping de l'image

