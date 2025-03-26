Technologies et langage de programmation
=======================================

Langage de programmation
------------------------

- **python** : Langage principal de programation du projet
- **HTML/CSS** : Pour les templates et les présentations
- **JavaScript** : Pour les intéraction coté client
- **SQL** : Pour les requêtes de la base de données via ORM Django

Framework et bibliothèques
------------------------

- **Django (Framework Web)** : Strucure principal de l'application (models-vue-template)
- **pytest** : Framework de test unitaire
- **flake8** : Outil de linting et d'analyse statique
- **Sentry SDK** : Bibliothèque d'intégration avec Sentry pour la surveillance des erreurs
- **logging** : Module standard python pour la journalisation


Système de base de données
--------------------------

- **SQlite3** : Base de données relationnelle légère utilisée en développement et production
- **Django ORM** : Interface de programmation pour la base de données SQlite3


Outils de déploiments et d'integration continue
----------------------------------------------

- **Docker** : Outil de virtualisation pour les conteneurs
- **Docker Compose** : Outil de gestion des conteneurs
- **GitHub Actions** : Outil de CI/CD pour les déploiments automatiques
- **Docker Hub** : Registre de conteneurs pour les déploiments
- **Render** : 


Outils de surveillance et de journalisation
----------------------------------------------

- **Sentry** : Outil de surveillance des erreurs et des logs
- **Logging Python ** : Journalisation des événements système et des erreurs


Environnements de développement
-------------------------------

- **Environnement virtuel Python (.venv)** : Isolation des dépendances
- **Docker** : Conteneurisation pour assurer la cohérence entre les environnements

Version des dépendances
-----------------------

(Vous pouvez retrouver les version des outils et bibliothèques utilisés dans le fichier `requirements.txt`)

.. code-block:: text

    django==3.0
    pytest-django==4.4.0
    flake8==3.9.2
    sentry-sdk==1.5.0
    # ... autres dépendances


Structure du projet
--------------------

La Structure du projet suit l'organisation standar d'un projet Django:

.. code-block:: text

    Python-OC-Lettings-FR/
    ├── lettings/                  # Application de gestion des locations
    │   ├── models.py              # Modèles de données pour les locations
    │   ├── views.py               # Vues pour les locations
    │   ├── urls.py                # Configuration des URLs
    │   └── tests.py               # Tests unitaires
    ├── profiles/                  # Application de gestion des profils
    │   ├── models.py              # Modèles de données pour les profils
    │   ├── views.py               # Vues pour les profils
    │   ├── urls.py                # Configuration des URLs
    │   └── tests.py               # Tests unitaires
    ├── templates/                 # Templates HTML
    ├── static/                    # Fichiers statiques (CSS, JS, images)
    ├── oc_lettings_site/          # Configuration principale du projet
    │   ├── settings.py            # Paramètres du projet
    │   ├── urls.py                # URLs principales
    │   └── wsgi.py                # Configuration WSGI
    ├── manage.py                  # Script de gestion Django
    ├── requirements.txt           # Dépendances du projet
    ├── docker-compose.yml         # Configuration Docker Compose
    ├── Dockerfile                 # Instructions de build Docker
    └── .env                       # Variable d'environnement