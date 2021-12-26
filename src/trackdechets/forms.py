import re

from django import forms
from django.core.exceptions import ValidationError

from .cuid import cuid

SIRET_LENGTH = 14

siret_pattern = re.compile(r"^\d{14}$")


def validate_siret(siret):
    siret = str(siret)
    length = len(siret)
    if length != SIRET_LENGTH:
        raise ValidationError(f"Siret must be 14 chars long, currently: {length}")
    if not siret_pattern.match(siret):
        raise ValidationError("Siret must only include 0-9 digits")


class ApplicationForm(forms.ModelForm):
    """Use a cuid as initial id on object creation to match prisma Ids"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial["id"] = cuid()


class AnonymousCompanyForm(forms.ModelForm):
    """Use a cuid as initial id on object creation to match prisma Ids"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial["id"] = cuid()

    def clean_siret(self):
        siret = self.cleaned_data["siret"]
        validate_siret(siret)
        return siret
