from django.db import models

from petstragram.main_app.validators import only_letters


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30
    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'
    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]
    GENDERS_MAX_LENGTH = max(len(x) for x, _ in GENDERS)

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            only_letters,
        )
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            only_letters,
        )
    )
    picture = models.URLField()
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=True,
        blank=True,
    )
    gender = models.CharField(
        max_length=GENDERS_MAX_LENGTH,
        null=True,
        blank=True,
        choices=GENDERS,
    )


class Pet(models.Model):
    PET_NAME_MAX_LENGTH = 30
    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'
    TYPE = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]
    TYPE_MAX_LENGTH = max(len(x) for x, _ in TYPE)

    name = models.CharField(
        max_length=PET_NAME_MAX_LENGTH,
    )
    type = models.CharField(
        max_length=TYPE_MAX_LENGTH,
        choices=TYPE,
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )





