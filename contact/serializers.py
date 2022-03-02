from rest_framework import serializers
from .models import Message
from rest_framework.exceptions import ValidationError


class MessageSerializer(serializers.ModelSerializer):

    def validate_date(self, value):
        if self.instance and self.instance.date != value:
            raise ValidationError("You may not edit date!")
        return value

    def create(self, validated_data):
        return Message.objects.create(**validated_data)

    class Meta:
        model = Message
        fields = [
            'id',
            'name',
            'email',
            'message',
        ]