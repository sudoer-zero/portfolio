from rest_framework import serializers
from .models import Logo, RandomImage


class LogoSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Logo
        fields = [
            'id',
            'created_by',
            'client',
            'description',
            'star',
            'creation_date',
            'get_image',
            'get_thumbnail',
            'get_absolute_url'
        ]


class RandomImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = RandomImage
        fields = [
            'id',
            'title',
            'get_image',
            'get_thumbnail'
        ]