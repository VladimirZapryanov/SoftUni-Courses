from django.core.validators import MinLengthValidator
from django.db import models

from my_plant.my_plant_app.validators import capital_letter_validator, only_letter_validator


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 10
    USERNAME_MIN_LENGTH = 2

    FIRST_NAME_MAX_LENGTH = 20

    LAST_NAME_MAX_LENGTH = 20

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(USERNAME_MIN_LENGTH),
        ),
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            capital_letter_validator,
        ),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            capital_letter_validator,
        ),
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Plant(models.Model):
    TYPE_MAX_LENGTH = 14

    OUTDOOR_PLANTS = 'Outdoor Plants'
    INDOOR_PLANTS = 'Indoor Plants'
    TYPE = [(x, x) for x in (OUTDOOR_PLANTS, INDOOR_PLANTS)]

    NAME_MAX_LENGTH = 20
    NAME_MIN_LENGTH = 2

    type = models.CharField(
        max_length=TYPE_MAX_LENGTH,
        choices=TYPE,
    )

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
            only_letter_validator,
        ),
    )

    image = models.URLField()

    description = models.TextField()

    price = models.FloatField()
