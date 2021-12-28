from django.db import models
from datetime import *
from versatileimagefield.fields import VersatileImageField
from tinymce.models import HTMLField


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

class Contact(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=120,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    text = models.TextField()

    def __str__(self):
        return str(self.name)






