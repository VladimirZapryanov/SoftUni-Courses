from django.contrib import admin

from my_plant.my_plant_app.models import Profile, Plant


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    pass