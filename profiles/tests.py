from django.test import TestCase, Client
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User


class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Paris')

    def test_profile_str(self):
        self.assertEqual(str(self.profile), 'testuser')


class ProfileViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Paris')

    def test_profile_index(self):
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Profiles')

    def test_profile_details(self):
        response = self.client.get(reverse('profiles:profile', args=[self.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')
        self.assertContains(response, 'Paris')

    def test_profiles_view_404(self):
        response = self.client.get(reverse('profiles:profile', args=['unknown']))
        self.assertEqual(response.status_code, 404)


class ProfilesIntegrationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Paris')

    def test_profiles_workflow(self):
        response = self.client.get(reverse("profiles:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Profiles")
        response = self.client.get(reverse("profiles:profile", args=[self.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')
        self.assertContains(response, 'Paris')
