import mock
from rest_framework import test
from rest_framework import status
from django import shortcuts

from api import factories


class ApiTestCase(test.APITestCase):
    """Test case for API."""

    MOCK_GET_DATA = mock.patch('api.views.RepositoriesView.get_data',
                               return_value=dict(factories.RepositoryFactory()))

    def setUp(self):
        self.owner = 'wieczorek1990'
        self.repository_name = 'wieczorek1990.github.io'

    @MOCK_GET_DATA
    def test_repositories(self, mock_get_data):
        response = self.client.get(shortcuts.reverse('repositories', kwargs={
            'owner': self.owner,
            'repository_name': self.repository_name,
        }))
        self.assertTrue(mock_get_data.called)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @MOCK_GET_DATA
    def test_no_repository_name(self, mock_get_data):
        response = self.client.get('/repositories/{owner}/'.format(
            owner=self.owner
        ))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @MOCK_GET_DATA
    def test_non_existing_repository(self, mock_get_data):
        response = self.client.get('/repositories/{owner}/{repository_name}'.format(
            owner=self.owner,
            repository_name='non-existing-repository-name',
        ))
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)
