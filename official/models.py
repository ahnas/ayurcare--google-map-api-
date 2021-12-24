from django.db import models
from versatileimagefield.fields import VersatileImageField



class Branch(models.Model):
    name       = models.CharField(max_length=255)
    title      = models.CharField(max_length=255)
    location   = models.CharField(max_length=255)
    latitude   = models.CharField(max_length=255)
    longitude  = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = ('Branches')

    def __str__(self):
        return str(self.name)