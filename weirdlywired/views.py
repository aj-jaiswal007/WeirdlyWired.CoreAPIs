from rest_framework.views import APIView, Response, status
from rest_framework.permissions import IsAuthenticated


class Test(APIView):
    def get(self, request):
        from django.conf import settings

        return Response(
            data={"message": "Hello this is demo"}, status=status.HTTP_200_OK
        )
