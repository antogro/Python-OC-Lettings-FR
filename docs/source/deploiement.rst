Déploiement et gestion de l'application
=====================================

Cette section détaille les procédures de déploiement et de gestion de l'application Orange County Lettings.


Processus CI/CD
-------------

L'application utilise GitHub Actions pour l'intégration continue et le déploiement continu.

Workflow de déploiement
~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
    │  Commit  │ ─── │   Tests  │ ─── │   Build  │ ─── │  Deploy  │
    └──────────┘     └──────────┘     └──────────┘     └──────────┘

1. **Commit** : Le développeur pousse du code vers le repository GitHub
2. **Tests** : Exécution automatique des tests unitaires et du linting
3. **Build** : Construction de l'image Docker si les tests sont réussis
4. **Deploy** : Publication de l'image sur Docker Hub

Configuration GitHub Actions
~~~~~~~~~~~~~~~~~~~~~~~~~

Le workflow est défini dans le fichier ``.github/