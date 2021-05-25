from typing import Any
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class BaseView(APIView):
    def data_response(self, message: str, data: Any) -> Response:
        return Response(
            data={"success": True, "message": message, "data": data},
            status=status.HTTP_200_OK,
        )

    def unauthorized_response(self, message: str) -> Response:
        return Response(
            data={"success": False, "message": message or "Unauthorized Access"},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    def forbidden_response(self, message: str) -> Response:
        return Response(
            data={
                "success": False,
                "message": message
                or "You do not have permission to perform this action.",
            },
            status=status.HTTP_403_FORBIDDEN,
        )
