# Projet application de médecine participative (Bee Patient)
![](https://github.com/data-IA-2022/Doctolib_Sylvine/blob/main/application/static/images/BeePatient.png)

Projet monté dans le cadre de la formation dev IA portée par Simplon et le Greta Val de Loire.

Ce projet a pour but de créer une application basée sur le framework Django pour construire une application de médecine participative, où des médecins gèrent un ensemble de patients qui doivent se connecter à intervalles définis afin de remplir des formulaires concernant divers aspects de santé. 

## Compétences visées
L’application présente trois cas d’utilisation principaux :

Un administrateur (en général le responsable d’un cabinet médical) attribue des comptes aux médecins qui le souhaitent. Il est en mesure de consulter le compte du médecin et de voir l’ensemble des patients suivis. ll peut crud des patients et des médecins. C’est lui qui attribue un patient à un médecin. Il peut voir l’historique des informations remplies par les patients dans un tableau possédant des filtres dynamiques.
Un médecin peut créer des comptes patients mais doit demander à l’administrateur pour qu’on les lui attribue. Le médecin peut crud les patients qui lui sont attribués. Il peut voir l’historique des informations remplies par les patients qu’il suit dans un tableau possédant des filtres dynamiques.
Un patient peut remplir le ou les formulaires sur la plateforme. Il peut voir l’historique de ses informations remplies dans un tableau possédant des filtres dynamiques.

​Chaque acteur doit s’authentifier sur la plateforme. Le patient et le médecin reçoivent un email avec les éléments permettant de s’authentifier. Lors de leur 1ère connexion, ils doivent modifier leur mot de passe.

​Aucune information personnelle n’est présente sur la plateforme. On utilisera un système d’ID pour cibler les comptes. Il leur est possible de réinitialiser leur mot de passe, et une recommandation de mot de passe est proposée sur la plateforme (avec 8 caractères dont chiffres, lettres minuscules et majuscules ainsi qu’un ou plusieurs symboles).

​
##  Données et base de données
La base de données sqlite intégrée dans Django se compose de trois tables principales, réparties dans les deux applications "authentification" et "application" :

![](https://github.com/data-IA-2022/Doctolib_Sylvine/blob/main/images/schema_bdd.png)

La table **Utilisateurs** comprend les informations de connexion de chaque utilisateur (username et mot de passe crypté avec Django), ainsi que leur rôle sur la plateforme qui déterminera leurs accès à différentes fonctionalités de l'appli:
* responsable = peut visualiser l'ensemble des données médicales entrées par les patients ; peut attribuer des patients à des médecins
* médecin = peut visualiser les données médicales uniquement des patients qui lui sont associés ; peut visualiser ces données sous forme graphique
* patient = peut visualiser uniquement ses propres données médicales ; peut accéder au formulaire pour entrer de nouvelles données.

Pour l'instant, cette table contient des données chargées dans la base à l'aide d'une fonction dans le views.py

La table **medecinPatients** permet de relier chaque patient au médecin qui le suit, les colonnes idMedecin et idPatient étant des foreignkey pointant vers username dans la table Utilisateurs.

La table **medData** contient les données médicales de chaque patient, avec notamment les champs suivants:
* anonymousID = l'identifiant du patient (foreignkey pointant vers username dans la table Utilisateurs)
* date = la date de remplissage du formulaire
* de nombreux champs concernant des données de nature médicale ou reliées au niveau de stress du patient

Pour l'instant, cette table contient des données fictives chargées dans la base à l'aide d'une fonction dans le views.py

## Installation
### Requirements
Cette version a pour le moment uniquement été testée dans un environnement Linux, dans une version 3.9.13 de Python.

Pour lancer ce programme, après avoir git clone le projet dans un répertoire local, créez un environnement virtuel dans le même répertoire:

`python -m venv venv`

puis activez-le:

`source venv/bin/activate`

Installez les requirements contenus dans le fichier requirements.txt

`pip install -r requirements.txt`


### Lancement du programme

- Commenter toutes les parties du code qui font des remplissage de tables à partir de csv : lignes tant à tant dans fichier1, ligne tant à tant dans fichier 2

- Faire les migrations sur la partie authentification:

`python manage.py makemigrations authentification`

`python manage.py migrate`
- Créer un superuser

`python manage.py createsuperuser`
- Décommenter les lignes tant à tant dans le fichier 1
- Lancer le programme pour remplir les tables dans authentification

`python manage.py runserver`
- Arrêter le serveur avec ctrl +c 
- Faire les migrations sur la partie application:
`python manage.py makemigrations application
python manage.py migrate`
- Décommenter les lignes tant à tant dans le fichier 2
- Lancer le programme pour remplir la table dans application

`python manage.py runserver`

- Le serveur tourne par défaut sur le port 8000 de votre machine. Pour y accéder, entrez cette adresse dans votre navigateur : http://127.0.0.1:8000/

- Pensez à attribuer le rôle responsable au superuser que vous avez créé. Vous pouvez faire celà en vous connectant sur http://127.0.0.1:8000/admin et en éditant l'instance admin dans la table Utilisateur

## Aperçus de l'application

Voici quelques screenshots de l'application:
![](https://github.com/data-IA-2022/Doctolib_Sylvine/blob/main/images/accueil.png)
![](https://github.com/data-IA-2022/Doctolib_Sylvine/blob/main/images/assoMedPat.png)
![](https://github.com/data-IA-2022/Doctolib_Sylvine/blob/main/images/vismed.png)
![](https://github.com/data-IA-2022/Doctolib_Sylvine/blob/main/images/form.png)
![](https://github.com/data-IA-2022/Doctolib_Sylvine/blob/main/images/compte.png)
![](https://github.com/data-IA-2022/Doctolib_Sylvine/blob/main/images/rgpd.png)

# Prochaines implémentations
La version présentée ici est une v1 avec peu de fonctionnalités. Les version futures contiendront:
* Périodicité de remplissage des formulaires : chaque médecin pourra choisir à quelle fréquence les patients pourront remplir leur formulaire. Le formulaire sera innaccessible aux patients hors de la bonne période
* Impossibilité pour les patients de modifier l'utilisateur ou la date du jour lors du remplissage (cacher les champs)
* Rendre fonctionnelle l'exploration graphique des données de façon interactive pour les médecins, voire incorporation d'intelligence artificielle pour analyser les données
* Envoi de mail pour inciter les nouveaux utilisateurs à changer leur mot de passe, via la page "Compte"
* Système empêchant les patients d'entrer des valeurs aberrantes dans le formulaire, et alerte envoyée au médecin si une valeur semble hors-norme
* Amélioration de l'aspect visuel du site (incorporation de css), notamment sur le contenu des pages 
* Effectuer des tests unitaires afind e vérifier que l'application est fonctionnelle


