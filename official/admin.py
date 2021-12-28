from django.contrib import admin
from .models import Branch,Doctor,Schedule
# Register your models here.

admin.site.register(Branch)
admin.site.register(Doctor)




@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('doctor',)}
    list_display = ('doctor','slug')