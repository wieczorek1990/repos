import unittest
import requests
from rest_framework import status


class RepositoriesTestCase(unittest.TestCase):
    """Tests the actual living localhost server instance."""

    HOST = 'http://localhost:8000'

    def test_wieczorek1990(self):
        response = requests.get(
            '{host}/repositories/wieczorek1990/wieczorek1990.github.io/'.format(
                host=self.HOST,
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertIsInstance(data['fullName'], str)
        self.assertIsNone(data['description'])
        self.assertIsInstance(data['cloneUrl'], str)
        self.assertIsInstance(data['stars'], int)
        self.assertIsInstance(data['createdAt'], str)


if __name__ == '__main__':
    unittest.main()
