from django.shortcuts import render, get_object_or_404
from .models import Profile
import logging
import sentry_sdk
from django.http import Http404

logger = logging.getLogger(__name__)


def index(request):
    """Affiche la liste des profils"""

    profiles_list = Profile.objects.all()
    return render(request, 'profiles/index.html', {'profiles_list': profiles_list})


def profile(request, username):
    """Affiche le profil d'un utilisateur"""
    try:
        profile = get_object_or_404(Profile, user__username=username)
        return render(request, 'profiles/profile.html', {'profile': profile})
    except Http404 as e:
        logging.warning(f"Erreur 404: {username}")
        sentry_sdk.capture_message(f"Erreur 404 - {username} profile introuvable")
        raise e
    except Exception as e:
        logging.error(f"Erreur lors de l'affichage du profil de {username}: {e}")
        sentry_sdk.capture_exception(e)
        return render(request, '500.html', status=500)
