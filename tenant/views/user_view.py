from tenant.serializers.user_serializer import UserBasicInfoSerializer
from tenant.models.user_model import User
from weirdlywired.common.base_view import BaseView


class UserView(BaseView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserBasicInfoSerializer(users, many=True)
        return self.data_response(message="All users", data=serializer.data)
