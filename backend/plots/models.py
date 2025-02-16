from django.contrib.gis.db import models
from django.conf import settings

class Plot(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    geom = models.PolygonField(srid=4326)  # Współrzędne działki
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class Building(models.Model):
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE)
    geom = models.PolygonField(srid=4326)  # Kształt budynku
    rotation = models.FloatField(default=0)  # Kąt obrotu
