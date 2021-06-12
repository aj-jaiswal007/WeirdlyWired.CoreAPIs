from django.db import models

from weirdlywired.models import BaseModel


class Tenant(BaseModel):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = "Tenant"
