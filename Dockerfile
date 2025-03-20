# Utilisation d'une image Python légère
FROM python:3.12-slim

# Définition du répertoire de travail
WORKDIR /app

# Empêcher la génération de fichiers .pyc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copie et installation des dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du reste des fichiers
COPY . /app

# Collecte des fichiers statiques après copie du code
RUN python manage.py collectstatic --noinput

# Exposition du port 8000
EXPOSE 8000

# Création d'un utilisateur non root
RUN adduser --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# Démarrage de Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]
