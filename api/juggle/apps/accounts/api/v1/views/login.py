from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from juggle.apps.accounts.api.permissions import IsNotAuthenticated
from juggle.apps.accounts.api.v1.serializers.login import LoginSerializer
from juggle.apps.accounts.services.login import LoginService


class LoginView(GenericAPIView):

    permission_classes = [IsNotAuthenticated]
    serializer_class = LoginSerializer

    @swagger_auto_schema(responses={status.HTTP_204_NO_CONTENT: openapi.Response("")})
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get("user")
        return LoginService.login(request, user)


class LogoutView(GenericAPIView):

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={status.HTTP_204_NO_CONTENT: openapi.Response("")})
    def post(self, request):
        return LoginService.logout(request)
