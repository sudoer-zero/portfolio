from .models import Project
from .serializers import ProjectSerializer
from rest_framework.generics import ListAPIView


class ProjectsList(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer