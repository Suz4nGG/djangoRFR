from projects.models import Project
from rest_framework import viewsets, permissions
from projects.serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
  queryset = Project.objects.all()
  permission_classes = [permissions.AllowAny]
  # * El como va a convertir los datos
  serializer_class = ProjectSerializer