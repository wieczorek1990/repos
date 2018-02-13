import github
from django.conf import settings
from rest_framework import views
from rest_framework import response
from rest_framework import status

from api import models
from api import serializers


class RepositoriesView(views.APIView):
    """View serving repository details."""

    @staticmethod
    def get_external_data(owner, repository_name):
        """Returns data for the serializer."""

        github_api = github.Github(settings.GITHUB_ACCESS_TOKEN)
        repository = github_api.get_repo(
            '{}/{}'.format(owner, repository_name), lazy=False
        )
        data = {
            'full_name': repository.full_name,
            'description': repository.description,
            'clone_url': repository.clone_url,
            'stars': repository.stargazers_count,
            'created_at': str(repository.created_at),
        }
        models.Repository.objects.get_or_create(
            owner=owner,
            data=data,
            repository_name=repository_name,
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
