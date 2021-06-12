from django.db import models

from chat.enums.model_enums import MessageType
from chat.models.room_model import Room
from tenant.models.user_model import User
from weirdlywired.models import BaseModel


class Message(BaseModel):
    message_type = models.IntegerField(
        choices=MessageType.choices, default=MessageType.TEXT
    )
    content = models.TextField(blank=False, null=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    class Meta:
        db_table = "Message"
