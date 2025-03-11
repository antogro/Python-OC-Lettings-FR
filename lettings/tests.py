from django.test import TestCase, Client
from django.urls import reverse
from lettings.models import Letting, Address


class LettingTestCase(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=10, street='rue de la Paix', city='Paris',
            zip_code=75000, state='FR', country_iso_code='FRA'
        )
        self.letting = Letting.objects.create(title='Bel appartement', address=self.address)

    def test_letting_str(self):
        self.assertEqual(str(self.letting), 'Bel appartement')

    def test_address_str(self):
        self.assertEqual(str(self.address), '10 rue de la Paix')


class LettingViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.address = Address.objects.create(
            number=10, street='rue de la Paix', city='Paris',
            zip_code=75000, state='FR', country_iso_code='FRA'
        )
        self.letting = Letting.objects.create(title='Bel appartement', address=self.address)

    def test_index_view(self):
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Lettings')

    def test_letting_view(self):
        response = self.client.get(reverse('lettings:letting', args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Bel appartement')
        self.assertContains(response, '10 rue de la Paix')

    def test_letting_view_404(self):
        response = self.client.get(reverse('lettings:letting', args=[999]))
        self.assertEqual(response.status_code, 404)


class LettingsIntegrationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.address = Address.objects.create(
            number=10, street='rue de la Paix', city='Paris',
            zip_code=75000, state='FR', country_iso_code='FRA'
        )
        self.letting = Letting.objects.create(title='Bel appartement', address=self.address)

    def test_lettings_workflow(self):
        response = self.client.get(reverse("lettings:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Lettings")
        response = self.client.get(reverse("lettings:letting", args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Bel appartement')
        self.assertContains(response, '10 rue de la Paix')
