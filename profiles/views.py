from django.shortcuts import render
from .models import Profile


def index(request):
    profiles_list = Profile.objects.all()
    return render(request, 'profiles/index.html', {'profiles_list': profiles_list})


def profile(request, username):
    profile = Profile.objects.get(user__username=username)
    return render(request, 'profiles/profile.html', {'profile': profile})
