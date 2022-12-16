from django.core.exceptions import ValidationError


def only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Your name must have only letters')