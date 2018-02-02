from rest_framework import views
from rest_framework import response

from api import serializers


class RepositoriesView(views.APIView):
    @staticmethod
    def get(request, owner=None, repository_name=None):
        # TODO(lwieczorek): implement
        from api import factories
        data = dict(factories.RepositoryFactory())

        serializer = serializers.RepositorySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return response.Response(data=serializer.data)
