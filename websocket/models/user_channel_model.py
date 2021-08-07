from tenant.models.user_model import User
from django.db import models

# Create your models here.
from weirdlywired.models import BaseModel


class UserChannel(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    channel_name = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        db_table = "UserChannel"
