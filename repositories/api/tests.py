from rest_framework import test
from rest_framework import status
from django import shortcuts


class ApiTestCase(test.APITestCase):
    def test_repositories(self):
        response = self.client.get(shortcuts.reverse('repositories', kwargs={
            'owner': 'wieczorek1990',
            'repository_name': 'wieczorek1990.github.io'
        }))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
