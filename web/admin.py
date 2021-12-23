from django.contrib import admin
from .models import Treatement,Gallery,Branch,Schedule,Doctor


@admin.register(Treatement)
class TreatementAdmin(admin.ModelAdmin):
    list_display =('title','summary')


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    pass


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    pass


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass