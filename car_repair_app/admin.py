from django.contrib import admin
from .models import Car, Repair


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    pass
