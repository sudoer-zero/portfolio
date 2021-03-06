from django.core.files import File
from django.db import models
from django.urls import reverse

from io import BytesIO
from PIL import Image

from autoslug import AutoSlugField
from ai_django_core.models import CommonInfo
from taggit.managers import TaggableManager

from back_end.settings import localhost


class Article(CommonInfo, models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique_with='description')
    description = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='uploads/covers', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/thumbnails/', blank=True, null=True)
    content = models.TextField()
    like = models.PositiveSmallIntegerField(default=0)
    heart = models.PositiveSmallIntegerField(default=0)
    happy = models.PositiveSmallIntegerField(default=0)
    tags = TaggableManager()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.slug}/'

    def creation_date(self):
        return self.created_at.strftime('%b %d, %y')

    def get_image(self):
        if self.image:
            return localhost + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return localhost + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return localhost + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(200, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'PNG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
