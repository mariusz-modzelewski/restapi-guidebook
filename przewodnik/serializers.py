from rest_framework import serializers
from .models import Event, Place, Address, Coordinates, EventType, PlaceType

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street','number','postalCode','city']

class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = ['x','y']

class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = ['id', 'name']

class PlaceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceType
        fields = ['id', 'name']

class EventSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=False)
    position = CoordinatesSerializer(many=False)
    type = EventTypeSerializer(many=False)
    class Meta:
        model = Event
        fields = ['id','title','organizer','desc','address','position',
                  'type','img','startDate','endDate','details','url']

class PlaceSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=False)
    position = CoordinatesSerializer(many=False)
    type = PlaceTypeSerializer(many=False)
    class Meta:
        model = Place
        fields = ['id','title','desc','address','position','type','img']