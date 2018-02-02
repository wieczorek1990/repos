from rest_framework import serializers


class RepositorySerializer(serializers.Serializer):
    """Repository serializer."""

    full_name = serializers.CharField()
    # repository may not have a description
    description = serializers.CharField(allow_null=True)
    clone_url = serializers.CharField()
    stars = serializers.IntegerField()
    created_at = serializers.DateTimeField()
