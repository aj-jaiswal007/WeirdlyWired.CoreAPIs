import json

from chat.enums.model_enums import RoomType
from tenant.models.user_model import User


class MessageEvent:
    def __init__(
        self,
        sender: User,
        content,
        receiver_id: int,
        receiver_type: int = RoomType.PERSONAL,
    ):
        self.sender = sender
        self.content = content
        self.receiver_id = receiver_id
        self.receiver_type = receiver_type

    @property
    def text(self):
        return json.dumps(
            {
                "sender_name": self.sender.username,
                "sender_id": self.sender.id,
                "content": self.content,
                "receiver_id": self.receiver_id,
                "receiver_type": self.receiver_type,
            }
        )
