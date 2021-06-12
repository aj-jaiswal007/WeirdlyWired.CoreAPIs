from django.db import models
from weirdlywired.models import BaseModel
from chat.enums.model_enums import RoomType


class Room(BaseModel):
    name = models.CharField(max_length=128)
    room_type = models.IntegerField(choices=RoomType.choices)
    info = models.JSONField()

    class Meta:
        db_table = "Room"
