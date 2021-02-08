from django.contrib import admin
from .models import Event, Place, Address, EventType, PlaceType, Coordinates

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id','title','organizer','startDate','endDate','type']
    list_filter = ['startDate','endDate','type']
    search_fields = ['id','title','organizer',
                     'startDate','endDate','type__name']

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['id','title','type','address']
    list_filter = ['type']
    search_fields = ['id','title','type__name','address__street',
                     'address__city','address__number',
                     'address__postalCode']

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['id','street','number','postalCode','city']
    search_fields = ['id','street','number','postalCode','city']

@admin.register(Coordinates)
class CoordinatesAdmin(admin.ModelAdmin):
    list_display = ['id','x','y']
    search_fields = ['id','x','y']

@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    search_fields = ['id','name']

@admin.register(PlaceType)
class PlaceTypeAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    search_fields = ['id','name']