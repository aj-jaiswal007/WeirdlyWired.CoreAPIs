from django.db import models

from chat.enums.model_enums import RoomMemberChatStatus, RoomMemberRole
from chat.models.room_model import Room
from tenant.models import User
from weirdlywired.models import BaseModel


class RoomMember(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    role = models.IntegerField(choices=RoomMemberRole.choices)
    status = models.IntegerField(
        choices=RoomMemberChatStatus.choices, default=RoomMemberChatStatus.ACTIVE
    )

    class Meta:
        db_table = "RoomMember"
