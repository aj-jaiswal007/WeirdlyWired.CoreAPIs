from django.db import models


class RoomType(models.IntegerChoices):
    PERSONAL = 0
    GROUP = 1
    PUBLIC = 2


class RoomMemberRole(models.IntegerChoices):
    ADMIN = 0
    MEMBER = 1


class RoomMemberChatStatus(models.IntegerChoices):
    ACTIVE = 0
    ARCHIVED = 1
    DELETED = 2


class MessageType(models.IntegerChoices):
    TEXT = 0
    IMAGE = 1
