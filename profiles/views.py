from django.shortcuts import render, get_object_or_404
from .models import Profile


def index(request):
    """Affiche la liste des profils"""

    profiles_list = Profile.objects.all()
    return render(request, 'profiles/index.html', {'profiles_list': profiles_list})


def profile(request, username):
    """Affiche le profil d'un utilisateur"""
    profile = get_object_or_404(Profile, user__username=username)
    return render(request, 'profiles/profile.html', {'profile': profile})
