from django.db import models

from weirdlywired.helpers.secrets_helper import get_random_key


class BaseModel(models.Model):
    key = models.CharField(max_length=32, unique=True, default=get_random_key)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
