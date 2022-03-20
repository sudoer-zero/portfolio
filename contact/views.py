from .serializers import MessageSerializer
from rest_framework import mixins
from rest_framework import generics
from .models import Message
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class MessagePost(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = MessageSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'home.html'
    login_url = '/users/login/'


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = 'contact/detail.html'
    login_url = '/users/login/'
