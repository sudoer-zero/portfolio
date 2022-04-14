from django.db import models
from autoslug import AutoSlugField
from back_end.settings import localhost


class Projects(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique_with='description')
    description = models.CharField(max_length=250)
    url = models.URLField()
    image = models.ImageField(upload='work/covers', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return localhost + self.image.url
        return ''
