from django.shortcuts import render
import sentry_sdk
import logging


logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'index.html')


def custom_404(request, exception):
    """Capture et log une erreur 404"""
    logger.warning(f"Erreur 404: {request.path}")
    sentry_sdk.capture_message(f"Erreur 404 sur {request.path}")
    return render(request, '404.html', status=404)


def custom_500(request):
    """Capture et log une erreur 500"""
    logger.warning(f"Erreur 404: {request.path}", exc_info=True)
    sentry_sdk.capture_exception(Exception("Erreur 500"))
    return render(request, '500.html', status=500)
