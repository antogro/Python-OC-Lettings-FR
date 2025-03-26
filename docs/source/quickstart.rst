Guide de démarrage rapide
=========================

Ce guide vous permet de démarrer rapidement l'application

Lancement de l'application
--------------------------

Après avoir installé l'appllication selon les instructions du chapitre précédent, vous pouvez la démarrer de plusieurs façons :

Avec l'environnement virtuel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    # environnement virtuel activé
    python manage.py runserver

avec Docker
~~~~~~~~~~~

.. code-block:: bash
    docker-compose up

L'application sera accessible à l'adresse http://localhost:8000

Structure des URL
------------------

- Page d'accueil : ``/``
- Liste des locations : ``/lettings``
- Détails d'une location : ``/lettings/<id>/``
- Liste des profils : ``/profiles/``
- Détails d'un profil : ``/profiles/<id>/``
- Interface administrateur : ``/admin/``

Accès à l'interface administrateur
----------------------------------

1. Ouvrez votre navigateur et rendez-vous à l'adresse http://localhost:8000/admin
2. Connectez-vous avec les identifiants suivants :
    - Utilisateur : ``admin``
    - Mot de passe : ``Abc1234!``