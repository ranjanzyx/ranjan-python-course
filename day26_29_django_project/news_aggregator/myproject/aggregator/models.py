# aggregator/models.py
from django.db import models

class Article(models.Model):
    guid = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    publication_date = models.DateTimeField()
    author = models.CharField(max_length=100, blank=True, null=True)
    source = models.CharField(max_length=255)
    url = models.URLField(max_length=500, blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True, null=True)

