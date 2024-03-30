from tenant.serializers.user_serializer import UserBasicInfoSerializer
from tenant.models.user_model import User
from common.base_view import BaseViewMixin
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView


class UserViewSet(ViewSet, BaseViewMixin):
    def list(self, request):
        r_user: User = request.user
        # TODO: only return those users in the friend list
        users = User.objects.filter(is_staff=False, is_superuser=False).exclude(
            id=r_user.id  # type: ignore
        )
        serializer = UserBasicInfoSerializer(users, many=True)
        return self.data_response(message="All users", data=serializer.data)

    def retrieve(self, request, pk=None):
        user = User.objects.get(id=pk)
        serializer = UserBasicInfoSerializer(user)
        return self.data_response(message="User details", data=serializer.data)


class ProfileView(APIView, BaseViewMixin):
    def get(self, request):
        serializer = UserBasicInfoSerializer(request.user)
        return self.data_response(message="User details", data=serializer.data)
