from weirdlywired.common.base_view import BaseView


class TempView(BaseView):
    def get(self, request):
        return self.data_response(
            message="Test success!",
            data="Hello {}!".format(request.GET.get("name") or "Guest"),
        )
