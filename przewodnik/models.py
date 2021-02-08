from django.db import models

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    street = models.CharField(max_length=40, null=True)
    number = models.CharField(max_length=8, null=True, blank=True)
    postalCode = models.CharField(max_length=6, null=True)
    city = models.CharField(max_length=20, null=True)
    class Meta:
        verbose_name = "Adres"
        verbose_name_plural = "Adresy"
    def __str__(self):
        if(self.number):
            return self.street + " " + self.number + ", " \
                   + self.postalCode + " " + self.city
        else: return self.street + ", " + self.postalCode + " " \
                     + self.city

class Coordinates(models.Model):
    id = models.AutoField(primary_key=True)
    x = models.DecimalField(decimal_places=6, max_digits=12, null=False)
    y = models.DecimalField(decimal_places=6, max_digits=12, null=False)
    class Meta:
        verbose_name = "Współrzędne"
        verbose_name_plural = "Współrzędne"
    def __str__(self):
        return str(self.x) + ", " + str(self.y)

class EventType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False, unique=True)
    class Meta:
        verbose_name = "Typ wydarzenia"
        verbose_name_plural = "Typy wydarzeń"
    def __str__(self):
        return self.name

class PlaceType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False, unique=True)
    class Meta:
        verbose_name = "Typ miejsca"
        verbose_name_plural = "Typy miejsc"
    def __str__(self):
        return self.name

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    organizer = models.CharField(max_length=40, blank=True)
    desc = models.TextField(max_length=1000)
    address = models.ForeignKey(Address, null=True, blank=True,
                                on_delete=models.CASCADE)
    position = models.ForeignKey(Coordinates, null=False,
                                 on_delete=models.CASCADE)
    type = models.ForeignKey(EventType, null=False,
                             on_delete=models.CASCADE)
    startDate = models.DateTimeField(null=False)
    endDate = models.DateTimeField(null=False)
    details = models.TextField(max_length=3000, null=False,
                               blank=True)
    img = models.ImageField(upload_to='img/events/', blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    class Meta:
        verbose_name = "Wydarzenie"
        verbose_name_plural = "Wydarzenia"
        unique_together = (('title','position'))
    def __str__(self):
        return self.title

class Place(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80)
    desc = models.TextField(max_length=1000)
    address = models.ForeignKey(Address,
                                null=True, blank=True,
                                on_delete=models.CASCADE)
    position = models.ForeignKey(Coordinates, null=False,
                                 on_delete=models.CASCADE)
    type = models.ForeignKey(PlaceType, on_delete=models.CASCADE,
                             null=False)
    img = models.ImageField(upload_to='img/places/', blank=True)
    class Meta:
        verbose_name = "Miejsce"
        verbose_name_plural = "Miejsca"
        unique_together = (('title','position'))
    def __str__(self):
        return self.title



