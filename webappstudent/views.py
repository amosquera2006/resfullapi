
from rest_framework import viewsets
from .serializers import studentSerializer
from . models import emplStud

# Create your views here.

class studentList(viewsets.ModelViewSet):

    queryset = emplStud.objects.all().order_by('firstname')
    serializer_class = studentSerializer

