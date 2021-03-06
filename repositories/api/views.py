import logging
import github
from django.conf import settings
from django.db import transaction
from rest_framework import views
from rest_framework import response
from rest_framework import status

from api import models
from api import serializers


GITHUB_API = github.Github(settings.GITHUB_ACCESS_TOKEN)


class RepositoriesView(views.APIView):
    """View serving repository details."""

    @staticmethod
    def get_external_data(owner, repository_name):
        """Returns data for the serializer."""

        repository = GITHUB_API.get_repo(
            '{}/{}'.format(owner, repository_name), lazy=False
        )
        data = {
            'full_name': repository.full_name,
            'description': repository.description,
            'clone_url': repository.clone_url,
            'stars': repository.stargazers_count,
            'created_at': str(repository.created_at),
        }
        with transaction.atomic():
            models.Repository.objects.get_or_create(
                owner=owner,
                repository_name=repository_name,
                defaults=dict(data=data),
            )
        return data

    @classmethod
    def get(cls, request, owner=None, repository_name=None):
        """Handles GET HTTP requests"""

        if owner is None or repository_name is None:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            repository = models.Repository.objects.filter(
                owner=owner,
                repository_name=repository_name,
            ).first()
            if repository is None:
                data = cls.get_external_data(owner, repository_name)
            else:
                data = repository.data
            serializer = serializers.RepositorySerializer(data=data)
            serializer.is_valid(raise_exception=True)
            return response.Response(data=serializer.data)
        except github.UnknownObjectException:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        except github.BadCredentialsException:
            logging.error('GITHUB_ACCESS_TOKEN is invalid')
            return response.Response(status=status.HTTP_400_BAD_REQUEST)
        except github.GithubException:  # this is the fallback exception
            logging.error('Github is down or something else is wrong')
            return response.Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
