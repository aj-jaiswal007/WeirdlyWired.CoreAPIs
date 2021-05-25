from rest_framework.views import APIView, Response, status
class Test(APIView):

    def get(self, request):
        from django.conf import settings
        return Response(data={
            "Key": settings.DEBUG,
            "h": settings.TEST
            }, status=status.HTTP_200_OK)
