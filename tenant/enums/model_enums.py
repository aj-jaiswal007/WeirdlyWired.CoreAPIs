from django.db import models


class MemberRoleType(models.IntegerChoices):
    ADMIN = 0
    TEAMMATE = 1
    GUEST = 2
