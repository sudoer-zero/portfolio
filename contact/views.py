from .serializers import MessageSerializer
from rest_framework import mixins
from rest_framework import generics


class MessagePost(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = MessageSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
