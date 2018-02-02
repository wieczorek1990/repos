import github
from django.conf import settings
from rest_framework import views
from rest_framework import response

from api import serializers


class RepositoriesView(views.APIView):
    """View serving repository details."""

    @staticmethod
    def get(request, owner=None, repository_name=None):
        github_api = github.Github(settings.GITHUB_ACCESS_TOKEN)
        repository = github_api.get_repo(
            '{}/{}'.format(owner, repository_name), lazy=False)
        data = {
            'full_name': repository.full_name,
            'description': repository.description,
            'clone_url': repository.clone_url,
            'stars': repository.stargazers_count,
            'created_at': repository.created_at,
        }
        serializer = serializers.RepositorySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return response.Response(data=serializer.data)
