from tenant.serializers.user_serializer import UserBasicInfoSerializer
from tenant.models.user_model import User
from weirdlywired.common.base_view import BaseView


class UserView(BaseView):
    def get(self, request):
        r_user: User = request.user
        print(r_user.__dict__)
        # TODO: only return those users in the friend list
        users = User.objects.all().exclude(id=r_user.id)
        serializer = UserBasicInfoSerializer(users, many=True)
        return self.data_response(message="All users", data=serializer.data)
