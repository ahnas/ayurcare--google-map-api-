from django.contrib import admin
from .models import Treatement,Gallery,Contact


@admin.register(Treatement)
class TreatementAdmin(admin.ModelAdmin):
    list_display =('title','summary')


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

