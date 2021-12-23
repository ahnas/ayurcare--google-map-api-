from django.db import models
from versatileimagefield.fields import VersatileImageField
from tinymce.models import HTMLField


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


class Treatement(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    image = VersatileImageField(upload_to = "Treatment")
    description = HTMLField(blank=True,null=True)

    def __str__(self):
        return str(self.title)


class Gallery(models.Model):
    image = VersatileImageField(upload_to ="Galleries")

    class Meta:
        verbose_name_plural = ('Gallery')

    def __str__(self):
        return str(self.image)


class Doctor(models.Model):
    register_number =models.IntegerField(unique=True)
    name = models.CharField(max_length=128)
    image = VersatileImageField(upload_to ='doctors')
    qualification = models.CharField(max_length=128)
    
    def __str__(self):
        return str(self.name)


class Schedule(models.Model):
    treatement = models.ForeignKey(Treatement,on_delete = models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str(self.treatement)
