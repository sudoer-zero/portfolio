from django.core.files import File
from django.db import models

from io import BytesIO
from PIL import Image

from autoslug import AutoSlugField
from ai_django_core.models import CommonInfo

from back_end.settings import localhost


class ImagePros:

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

    def make_thumbnail(self, image, size=(400, 400)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'PNG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail


class Logo(CommonInfo, ImagePros, models.Model):
    client = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='client', unique_with='description')
    description = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='uploads/logos', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/logos/thumbnails/', blank=True, null=True)
    star = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.client

    def get_absolute_url(self):
        return f'/{self.slug}/'

    def creation_date(self):
        return self.created_at.strftime('%b %d, %y')


class RandomImage(CommonInfo, ImagePros, models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/logos', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/logos/thumbnails/', blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

