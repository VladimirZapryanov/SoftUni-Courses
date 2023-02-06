<<<<<<< HEAD
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
=======
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
>>>>>>> c4cb2de84e4d95aeb5b1129c1cbc97122a654357
