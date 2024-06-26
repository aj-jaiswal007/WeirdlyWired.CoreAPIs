from typing import Union, Any, Optional

from rest_framework import status
from rest_framework.response import Response


class BaseViewMixin:
    def data_response(self, message: str, data: Any) -> Response:
        return Response(
            data={"success": True, "message": message, "data": data},
            status=status.HTTP_200_OK,
        )

    def unauthorized_response(self, message: Optional[str] = None) -> Response:
        return Response(
            data={"success": False, "message": message or "Unauthorized Access"},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    def forbidden_response(self, message: Optional[str] = None) -> Response:
        return Response(
            data={
                "success": False,
                "message": message
                or "You do not have permission to perform this action.",
            },
            status=status.HTTP_403_FORBIDDEN,
        )

    def bad_request_response(
        self, message: str, errors: Optional[list[Any]] = None
    ) -> Response:
        return Response(
            data={
                "success": False,
                "message": message,
                "errors": errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def not_found_response(self, message: Union[dict, list, str]) -> Response:
        return Response(
            data={
                "success": False,
                "message": message,
            },
            status=status.HTTP_404_NOT_FOUND,
        )
