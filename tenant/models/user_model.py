from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from tenant.managers import UserManager
from weirdlywired.helpers.secrets_helper import get_random_key


class User(AbstractUser):
    key = models.CharField(max_length=32, unique=True, default=get_random_key)
    email = models.EmailField(_("email address"), unique=True)
    # TODO: add required fields here
    phone = models.CharField(max_length=16, unique=False, blank=True, null=True)

    REQUIRED_FIELDS = ["email", "first_name", "last_name"]
    objects = UserManager()

    def __str__(self) -> str:
        return self.email

    class Meta:
        db_table = "user"
