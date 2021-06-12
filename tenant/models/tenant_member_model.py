from django.db import models

from tenant.enums.model_enums import MemberRoleType
from tenant.models.tenant_model import Tenant
from weirdlywired.models import BaseModel

from .user_model import User


class TenantMember(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    role = models.IntegerField(choices=MemberRoleType.choices)

    class Meta:
        db_table = "TenantMember"
