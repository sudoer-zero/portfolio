from django.shortcuts import render
import random
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin
from rest_framework.decorators import api_view

from django.http import Http404

from .serializers import LogoSerializer
from .models import Logo


class LogoListView(APIView):
    def get(self, request, format=None):
        logos = Logo.objects.all()
        serializer = LogoSerializer(logos, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def logo_star(request, pk):
    logo = get_object_or_404(Logo, pk=pk)
    logo.star += 1
    logo.save()
    data = {
        'success': True
    }
    return Response(data)
