from tenant.models.tenant_model import Tenant
from weirdlywired.models import BaseModel
from django.db import models
from .user_model import User
from tenant.enums.model_enums import MemberRoleType


class TenantMember(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    role = models.IntegerField(max_length=16, choices=MemberRoleType.choices)

    class Meta:
        db_table = "TenantMember"
