import datetime as dt
import re

from django import forms
from django.core.exceptions import ValidationError
from django_json_widget.widgets import JSONEditorWidget

from .cuid import cuid
from .models import Anonymouscompany, Bsdasri, Company, User

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
    """Use a cuid as id on object creation to match prisma Ids"""

    class Meta:
        model = Anonymouscompany
        exclude = [
            "id",
        ]
        widgets = {
            "siret": forms.TextInput(),
            "name": forms.TextInput(),
            "libellenaf": forms.TextInput(),
            "codenaf": forms.TextInput(),
            "codecommune": forms.TextInput(),
        }

    def clean_siret(self):
        siret = self.cleaned_data["siret"]
        validate_siret(siret)
        return siret

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.id:
            instance.id = cuid()
        if commit:
            instance.save()

        return instance


class CompanyForm(forms.ModelForm):
    """Use a cuid as initial id on object creation to match prisma Ids"""

    class Meta:
        model = Company
        exclude = [
            "id",
        ]
        widgets = {
            "siret": forms.TextInput(),
            "name": forms.TextInput(),
            "securitycode": forms.TextInput(),
            "gerepid": forms.TextInput(),
            "codenaf": forms.TextInput(),
            "contactemail": forms.TextInput(),
            "contactphone": forms.TextInput(),
            "website": forms.TextInput(),
            "givenname": forms.TextInput(),
            "ecoorganismeagreements": forms.TextInput(),
            "companytypes": forms.TextInput(),
            "verificationcode": forms.TextInput(),
            "verificationstatus": forms.TextInput(),
            "verificationmode": forms.TextInput(),
            "verificationcomment": forms.TextInput(),
        }

    def clean_siret(self):
        siret = self.cleaned_data["siret"]
        validate_siret(siret)
        return siret

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.id:
            instance.id = cuid()
        if commit:
            instance.save()
            self.save_m2m()

        return instance


class UserForm(forms.ModelForm):
    """Use a cuid as initial id on object creation to match prisma Ids"""

    class Meta:
        model = User
        exclude = ["id", "createdat", "updatedat", "activatedat"]
        widgets = {
            "email": forms.TextInput(),
            "name": forms.TextInput(),
            "phone": forms.TextInput(),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.id:
            instance.id = cuid()
            instance.isadmin = False
            instance.isactive = True
            instance.createdat = dt.datetime.now()
            instance.activatedat = dt.datetime.now()

        instance.updatedat = dt.datetime.now()
        if commit:
            instance.save()
            self.save_m2m()

        return instance


class BsdasriForm(forms.ModelForm):
    """Use a cuid as initial id on object creation to match prisma Ids"""

    class Meta:
        model = Bsdasri
        exclude = [
            "id",
            "createdat",
            "updatedat",
            "emitterwastepackagings",
            "transporterwastepackagings",
            "transporteracceptationstatus",
            "destinationwastepackagings",
            "destinationreceptionacceptationstatus",
        ]
        widgets = {
            "status": forms.TextInput,
            "emittercompanyname": forms.TextInput,
            "emittercompanysiret": forms.TextInput,
            "emittercompanycontact": forms.TextInput,
            "emittercompanyphone": forms.TextInput,
            "emittercompanymail": forms.TextInput,
            "emitterpickupsitename": forms.TextInput,
            "emitterpickupsitecity": forms.TextInput,
            "emitterpickupsitepostalcode": forms.TextInput,
            "wastecode": forms.TextInput,
            "wasteadr": forms.TextInput,
            # 'emitterwastepackagings': JSONEditorWidget,
            "emitteremissionsignatureauthor": forms.TextInput,
            "transportercompanyname": forms.TextInput,
            "transportercompanysiret": forms.TextInput,
            "transportercompanyphone": forms.TextInput,
            "transportercompanycontact": forms.TextInput,
            "transportercompanymail": forms.TextInput,
            "transporterrecepissenumber": forms.TextInput,
            "transporterrecepissedepartment": forms.TextInput,
            # "transporteracceptationstatus": forms.TextInput,
            # "transporterwastepackagings": JSONEditorWidget,
            "transportertransportsignatureauthor": forms.TextInput,
            "destinationcompanyname": forms.TextInput,
            "destinationcompanysiret": forms.TextInput,
            "destinationcompanycontact": forms.TextInput,
            "destinationcompanyphone": forms.TextInput,
            "destinationcompanymail": forms.TextInput,
            "destinationwastepackagings": JSONEditorWidget,
            "destinationreceptionacceptationstatus": forms.TextInput,
            "destinationreceptionwasterefusalreason": forms.TextInput,
            "destinationoperationcode": forms.TextInput,
            "destinationreceptionsignatureauthor": forms.TextInput,
            "transportertransportmode": forms.TextInput,
            "ecoorganismename": forms.TextInput,
            "ecoorganismesiret": forms.TextInput,
            "transportertransportplates": forms.TextInput,
            "identificationnumbers": forms.TextInput,
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.id:
            instance.id = cuid()

        instance.updatedat = dt.datetime.now()
        if commit:
            instance.save()
            self.save_m2m()

        return instance
