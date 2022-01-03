from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .constants import USER_BUSINESS, USER_DEVELOPPER, USER_SUPERADMIN
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Base class for all user models."""

    USER_CHOICES = (
        (USER_SUPERADMIN, _("Superadmin")),
        (USER_DEVELOPPER, _("Developper")),
        (USER_BUSINESS, _("Business")),
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    first_name = models.CharField(_("User first name"), max_length=250)
    last_name = models.CharField(_("User last name"), max_length=250)
    is_active = models.BooleanField(
        _("active"), default=True, help_text=_("Should this user be treated as active.")
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Can the user log into this admin site."),
    )
    category = models.CharField(
        _("category"), max_length=20, choices=USER_CHOICES, default=USER_DEVELOPPER
    )
    email = models.EmailField(_("Email address"), unique=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        app_label = "accounts"

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    @property
    def is_superadmin(self):
        return self.category == USER_SUPERADMIN

    @property
    def is_developper(self):
        return self.category == USER_DEVELOPPER

    @property
    def is_business(self):
        return self.category == USER_BUSINESS
