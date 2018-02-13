from django.db import models
from django.contrib.postgres import fields


class Repository(models.Model):
    owner = models.TextField()
    repository_name = models.TextField()
    data = fields.JSONField()
