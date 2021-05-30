from weirdlywired.common.base_view import BaseView


class TestChatView(BaseView):
    def get(self, request):
        return self.data_response("Done", {})
