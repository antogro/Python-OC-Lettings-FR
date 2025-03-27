Guide d'utilisation
=================

Ce guide décrit les fonctionnalités principales de l'application Orange County Lettings et comment les utiliser.


Développement local
-------------------

**Prérequis :**
- Compte GitHub avec accès en lecture
- Git CLI, SQLite3, Python ≥ 3.6
- Docker & Docker Compose

**macOS / Linux :**

.. code-block:: bash

   git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git
   cd Python-OC-Lettings-FR
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   python manage.py runserver

- Aller sur : http://localhost:8000

**Utilisation de Docker :**

.. code-block:: bash

   docker-compose up --build
   docker-compose -f docker-compose.debug.yml up --build

**Windows (PowerShell) :**

.. code-block:: powershell
    .venv\Scripts\activate


Linting
-------

.. code-block:: bash

   flake8

Tests unitaires
---------------

.. code-block:: bash

   pytest

Panel d'administration
----------------------

- URL : http://localhost:8000/admin
- Utilisateur : `admin` / Mot de passe : `Abc1234!`

CI/CD
-----

- Lint + Tests sur chaque push
- Docker image build + push si succès

Surveillance et logs
--------------------

- Sentry (`SENTRY_DSN`)
- Fichier `logs/django_errors.log`

Déploiement
-----------

.. code-block:: bash

   docker pull amtao/oc_lettings_site:latest
   docker run -p 8000:8000 amtao/oc_lettings_site:latest

Base de données
---------------

.. code-block:: bash

   sqlite3 oc-lettings-site.sqlite3
   .tables
   .quit

Routes principales
------------------

- `/` : Accueil
- `/lettings/` : Locations
- `/profiles/` : Profils
- `/admin/` : Admin Django

Contact
-------

En cas de problème, ouvrez une issue sur GitHub.
