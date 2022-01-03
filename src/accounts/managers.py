from django.contrib.auth.models import BaseUserManager
from django.utils import timezone

from .constants import USER_SUPERADMIN


class UserManager(BaseUserManager):
    use_for_related_fields = True

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        """Creates a superuser with the given email and password."""
        now = timezone.now()
        if not email:
            raise ValueError("The email is a required field and cannot be empty")
        if not last_name or not first_name:
            raise ValueError("You cannot create users with no names")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_active=True,
            is_staff=True,
            is_superuser=True,
            category=USER_SUPERADMIN,
            date_joined=now,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email):
        lookup = f"{self.model.USERNAME_FIELD}__iexact"
        return self.get(**{lookup: email})
