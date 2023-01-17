from django.contrib import admin

from petstragram.main_app.models import Profile, Pet, PetPhoto


class PetInLineAdmin(admin.StackedInline):
    model = Pet


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = (PetInLineAdmin,)
    list_display = ('first_name', 'last_name')


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    pass
