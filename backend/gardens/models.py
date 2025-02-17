from django.db import models
from django.contrib.gis.db import models as gis_models

class Plant(models.Model):
    SOIL_CHOICES = [
        ('sandy', 'Piaszczysta'),
        ('clay', 'Gliniana'),
        ('loamy', 'Próchnicza')
    ]
    
    name = models.CharField(max_length=100, verbose_name="Nazwa rośliny")
    watering_interval = models.PositiveIntegerField(verbose_name="Podlewanie co (dni)")
    soil_type = models.CharField(max_length=20, choices=SOIL_CHOICES)
    optimal_sunlight = models.CharField(max_length=50, verbose_name="Nasłonecznienie")
    geom = gis_models.PointField(srid=4326, verbose_name="Lokalizacja na mapie")

    def __str__(self):
        return self.name
