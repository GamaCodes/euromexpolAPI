from rest_framework import viewsets
from .models import dynamicCode
from .serializer import DynamicSerializer

# Create your views here.

class DynamicViewSet(viewsets.ModelViewSet):
    serializer_class = DynamicSerializer
    queryset = dynamicCode.objects.all()