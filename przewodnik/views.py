from django.http import HttpResponseRedirect
from rest_framework import viewsets
from .serializers import EventSerializer, PlaceSerializer,\
    PlaceTypeSerializer, EventTypeSerializer
from .models import Event, Place, PlaceType, EventType

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

def site_redirect(request):
    return HttpResponseRedirect("http://localhost:3000")

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class PlaceViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class PlaceTypesViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceTypeSerializer
    queryset = PlaceType.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class EventTypesViewSet(viewsets.ModelViewSet):
    serializer_class = EventTypeSerializer
    queryset = EventType.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)