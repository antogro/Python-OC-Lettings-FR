from django.shortcuts import render, get_object_or_404
from .models import Letting
import logging
import sentry_sdk
from django.http import Http404

logger = logging.getLogger(__name__)


def index(request):
    """Affiche la liste des annonces"""
    lettings_list = Letting.objects.all()
    return render(request, "lettings/index.html", {"lettings_list": lettings_list})


def letting(request, letting_id):
    """Affiche les détails d'une annonce"""
    try:
        letting = get_object_or_404(Letting, id=letting_id)
        context = {
            "title": letting.title,
            "address": letting.address,
        }
        return render(request, "lettings/letting.html", context)
    except Http404 as e:
        logging.warning(f"Erreur 404: {letting_id}")
        sentry_sdk.capture_message(f"Erreur 404 - {letting_id} annonce introuvable")
        raise e
    except Exception as e:
        logging.error(f"Erreur lors de l'affichage de l'annonce {letting_id}: {e}")
        sentry_sdk.capture_exception(e)
        return render(request, "500.html", status=500)
