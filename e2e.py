import unittest
import re
import requests
from rest_framework import status


class RepositoriesTestCase(unittest.TestCase):
    """Tests the actual living localhost server instance."""

    HOST = 'http://localhost:8000'

    def assertIsUrl(self, string):
        return string.startswith('https://')

    def assertIsISO8601(self, string):
        return re.match(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', string)

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
        self.assertIsUrl(data['cloneUrl'])
        self.assertIsInstance(data['stars'], int)
        self.assertIsInstance(data['createdAt'], str)
        self.assertIsISO8601(data['createdAt'])

    def test_torvalds(self):
        response = requests.get(
            '{host}/repositories/torvalds/linux/'.format(
                host=self.HOST,
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertIsInstance(data['fullName'], str)
        self.assertIsInstance(data['description'], str)
        self.assertIsInstance(data['cloneUrl'], str)
        self.assertIsUrl(data['cloneUrl'])
        self.assertIsInstance(data['stars'], int)
        self.assertIsInstance(data['createdAt'], str)
        self.assertIsISO8601(data['createdAt'])


if __name__ == '__main__':
    unittest.main()
