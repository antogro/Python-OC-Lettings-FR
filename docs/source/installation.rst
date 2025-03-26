Installation
============

Prérequis
----------

- Compte GitHub
- Git Cli installé
- SQlite3 Cli pour la gestion de la base de données
- Python 3.12
- Docker

Clonage du repository
--------------------

.. code-block:: bash
    git clone https://github.com/antogro/Python-OC-Lettings-FR.git
    cd Python-OC-Lettings-FR


Installation de l'environnement virtuel
---------------------------------------

macOs / Linux

.. code-block:: bash

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

Windows 

.. code-block:: bash

    python -m venv venv
    .venv\Scripts\activate
    pip install -r requirements.txt


Vérification de l'installation
--------------------------------

Pour vérifier que l'installation est correcte, vous pouvez exécuter les commandes suivantes :

.. code-block:: bash

    python manage.py test

Et le linting : 

.. code-block:: bash

    flake8 --exclude=static,.venv .

Si les tests et le linting s'executent sans erreur, l'installation est réussi.

Configuration de l'environnement
------------------------------

Certaines Variables d'environnement sont nécessaires pour le bon fonctionnement de l'application

Pour configurer ces variables, vous pouvez:
- Créer un fichier ``.env`` dans le dossier racine du projet
- Ajouter la variable necessaire

Exemple de fichier ``.env`` : 

.. code-block:: text
    SENTRY_DSN=https://votre-cle@sentry.io/votre-projet
