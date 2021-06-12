from django.db import models

from chat.enums.model_enums import RoomType
from weirdlywired.models import BaseModel


class Room(BaseModel):
    name = models.CharField(max_length=128)
    room_type = models.IntegerField(choices=RoomType.choices)
    info = models.JSONField()

    class Meta:
        db_table = "Room"
