from django.urls import path, include
from rest_framework import routers
from .views import EventViewSet, PlaceViewSet, PlaceTypesViewSet, EventTypesViewSet

router = routers.DefaultRouter()
router.register('event', EventViewSet)
router.register('place', PlaceViewSet)
router.register('placetypes', PlaceTypesViewSet)
router.register('eventtypes', EventTypesViewSet)

urlpatterns = [
    path('', include(router.urls))
]
