from django.db import models
from taggit.managers import TaggableManager


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    gh_url = models.URLField()
    status = models.CharField(max_length=100, blank=True)
    prog_lang = TaggableManager()

    def __str__(self):
        return self.name
