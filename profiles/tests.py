from django.test import TestCase, Client
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User


class ProfileTestCase(TestCase):
    """Création d'un utilisateur et d'un profil"""
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Paris')

    def test_profile_str(self):
        """test de la méthode __str__ de Profile"""
        self.assertEqual(str(self.profile), 'testuser')


class ProfileViewTestCase(TestCase):
    def setUp(self):
        """Création d'un utilisateur et d'un profil"""
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Paris')

    def test_profile_index(self):
        """Test de la vue index"""
#         # On teste que la vue retourne un code 200 et contient le mot 'Profiles'
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Profiles')

    def test_profile_details(self):
        """Test de la vue profile"""
        # On teste que la vue retourne un code 200 et
        # contient le nom d'utilisateur et la ville favorite
        response = self.client.get(reverse('profiles:profile', args=[self.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')
        self.assertContains(response, 'Paris')

    def test_profiles_view_404(self):
        """Test de la vue profile avec un utilisateur inconnu"""
        # On teste que la vue retourne un code 404
        response = self.client.get(reverse('profiles:profile', args=['unknown']))
        self.assertEqual(response.status_code, 404)


class ProfilesIntegrationTestCase(TestCase):
    def setUp(self):
        """Création d'un utilisateur et d'un profil"""
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Paris')

    def test_profiles_workflow(self):
        """Test de l'affichage de la liste des profils et d'un profil"""
        # On teste que la vue profile retourne un code 200 et contient
        # le nom d'utilisateur et la ville favorite
        response = self.client.get(reverse("profiles:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Profiles")
        response = self.client.get(reverse("profiles:profile", args=[self.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')
        self.assertContains(response, 'Paris')
