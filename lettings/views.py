from django.shortcuts import render, get_object_or_404
from .models import Letting


def index(request):
    """Affiche la liste des annonces"""
    lettings_list = Letting.objects.all()
    return render(request, "lettings/index.html", {"lettings_list": lettings_list})


def letting(request, letting_id):
    """Affiche les détails d'une annonce"""
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
