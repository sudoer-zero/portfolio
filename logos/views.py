import random

from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import LogoSerializer, RandomImageSerializer
from .models import Logo, RandomImage


class LogoListView(APIView):
    def get(self, request, format=None):
        logos = Logo.objects.all()
        serializer = LogoSerializer(logos, many=True)
        return Response(serializer.data)


class LatestLogosList(ListAPIView):
    queryset = Logo.objects.all()[0:3]
    serializer_class = LogoSerializer


@api_view(['POST'])
def logo_star(request, pk):
    logo = get_object_or_404(Logo, pk=pk)
    logo.star += 1
    logo.save()
    data = {
        'success': True
    }
    return Response(data)


class RandomImageView(ListAPIView):

    def get_queryset(self):
        id_list = list(RandomImage.objects.all().values_list('id', flat=True))
        random_id = random.choice(id_list)
        return RandomImage.objects.all().filter(id=random_id)
    serializer_class = RandomImageSerializer
