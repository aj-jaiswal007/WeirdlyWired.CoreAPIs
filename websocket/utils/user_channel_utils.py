from websocket.models import UserChannel
from channels.db import DatabaseSyncToAsync


class UserChannelUtils:
    @DatabaseSyncToAsync
    def get_channel_by_user_id(self, user_id) -> UserChannel:
        return UserChannel.objects.get(user_id=user_id)

    @DatabaseSyncToAsync
    def update_channel_name_for_user(self, user_id, channel_name) -> UserChannel:
        try:
            uc = UserChannel.objects.get(user_id=user_id)
        except UserChannel.DoesNotExist:
            uc = UserChannel(user_id=user_id)

        uc.channel_name = channel_name
        uc.save()
        return uc
