## Résumé

Site web d'Orange County Lettings, permettant la gestion des locations et profils.

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure
- Docker et Docker Compose

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (sauf si un environnement virtuel est activé).

### macOS / Linux

#### Cloner le repository

```sh
cd /path/to/put/project/in
git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git
```

#### Créer l'environnement virtuel

```sh
cd /path/to/Python-OC-Lettings-FR
python -m venv venv
source venv/bin/activate
pip install --requirement requirements.txt
```

#### Exécuter le site

```sh
python manage.py runserver
```

Aller sur `http://localhost:8000` dans un navigateur.

#### Utilisation de Docker

##### Exécution en mode normal

```sh
docker-compose up --build
```

##### Exécution en mode debug

```sh
docker-compose -f docker-compose.debug.yml up --build
```

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel : `venv\Scripts\Activate.ps1`

## Linting

```sh
flake8
```

## Tests unitaires

```sh
pytest
```

## Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

## CI/CD avec GitHub Actions

Un pipeline CI/CD est en place pour :

1. Exécuter des tests unitaires et du linting sur chaque push et pull request.
2. Construire et pousser l'image Docker sur Docker Hub si les tests sont réussis.
3. Lancer un déploiement automatique via un webhook Render.

### Secrets GitHub Actions requis

Ajoutez les secrets suivants dans la configuration GitHub du dépôt :

- `DOCKER_USERNAME` : Nom d'utilisateur Docker Hub
- `DOCKER_PAT` : Token d'accès personnel Docker Hub
- `RENDER_DEPLOY_HOOK` : URL du webhook Render pour déclencher le déploiement

## Surveillance et journalisation

L'application intègre Sentry pour la capture et la surveillance des erreurs.

- Assurez-vous que la variable d'environnement `SENTRY_DSN` est correctement configurée dans le fichier `.env`.
- Les logs sont également enregistrés dans `logs/django_errors.log`.

### Fichier `.env`

Ajoutez un fichier `.env` à la racine du projet avec le contenu suivant tel que le fichier `.env.example` :

```env
SENTRY_DSN=
```

## Déploiement

L'image Docker est déployée automatiquement après validation des tests CI/CD sur Docker Hub.
Vous pouvez extraire l'image et l'exécuter avec :

```sh
docker pull <dockerhub_username>/oc_lettings_site:latest
docker run -p 8000:8000 <dockerhub_username>/oc_lettings_site:latest
```

Remplacez `<dockerhub_username>` par le nom d'utilisateur Docker Hub utilisé dans le pipeline CI/CD.

## Base de données

L'application utilise SQLite par défaut. Pour interagir avec la base de données :

```sh
sqlite3 oc-lettings-site.sqlite3
.tables  # Afficher les tables
.quit  # Quitter
```

## Routes principales

- `/` : Page d'accueil
- `/lettings/` : Liste des locations
- `/lettings/<int:letting_id>/` : Détail d'une location
- `/profiles/` : Liste des profils
- `/profiles/<str:username>/` : Détail d'un profil
- `/admin/` : Interface d'administration Django

## Contact

En cas de problème, veuillez contacter l'administrateur du projet ou ouvrir une issue sur GitHub.