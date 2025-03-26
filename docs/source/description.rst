Description du projet
=====================

Aperçu
--------

Orange Conty Lettings est une application web permettant au utilisateur de pouvoir gérer des locations imobilières et leurs profils utilisateurs.
L'application permet de consilter les annonces de locations disponibles et de créer leurs profiles avec leurs préferences.

fonctionnalités principales
-----------------------------

- Afficahge d'une liste de locations disponibles
- Consultation des détails d'une location spécifique
- Affichage d'une liste de profils utilisateurs
- Consultation des détails d'un profil spécifique
- Interface d'administration pour la gestion des données

Architecture
-------------
L'application est structurée selon le modèle MVT (Modèle-Vue-Template) de Django avec :

**models** : définit les structures de données pour les locations et les profils utilisateurs
**views** : Logique de traitement des requêtes HTTP
**templates** : définit les vues HTML pour les pages de l'application

Divisé en deux modules principaux : 

1. **lettings**: Gestion des locations et des adresses
2. **profiles**: Gestion des profils utilisateurs

Objectifs du projet:
--------------------

- Fournir une interface utilisateur conviviale pour la gestion des locations et des profils utilisateurs
- Assurer une maintenance facile gràce à une documentation complète
- Mettre en place un processus de CI/CD robuste pour les déploiements
- Intégrer un système de surveillance et de journalisation pour le suivi des erreurs