from rest_framework import serializers


class RepositorySerializer(serializers.Serializer):
    full_name = serializers.CharField()
    description = serializers.CharField()
    clone_url = serializers.CharField()
    stars = serializers.IntegerField()
    created_at = serializers.DateTimeField()
