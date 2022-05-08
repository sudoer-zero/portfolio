from rest_framework import serializers
from .models import Project
from taggit.serializers import (TaggitSerializer, TagListSerializerField)


class ProjectSerializer(TaggitSerializer, serializers.ModelSerializer):
    prog_lang = TagListSerializerField()

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'description',
            'gh_url',
            'status',
            'prog_lang',
        ]