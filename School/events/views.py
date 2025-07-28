from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Event
from .serializers import EventSerializer
from .permissions import IsAdminOrSubadmin

# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('-event_date')
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsAdminOrSubadmin]

