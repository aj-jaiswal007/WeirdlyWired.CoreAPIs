from common.base_view import BaseViewMixin
from rest_framework.views import APIView


class TestChatView(APIView, BaseViewMixin):
    def get(self, request):
        return self.data_response("Done", {})
