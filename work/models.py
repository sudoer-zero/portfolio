import requests
from django.db import models
from taggit.managers import TaggableManager


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    readme_url = models.URLField(blank=True)
    gh_url = models.URLField()
    status = models.CharField(max_length=100, blank=True)
    prog_lang = TaggableManager()

    class Meta:
        ordering = ['-status']

    def __str__(self):
        return self.name

    def get_readme(self):
        url = requests.get(self.readme_url)
        return url.text