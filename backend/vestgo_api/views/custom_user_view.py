from django.contrib.auth.models import Group
from rest_framework import status, generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import AuthenticationFailed

from rest_framework_simplejwt.views import TokenObtainPairView

from vestgo_api.models import CustomUser
from vestgo_api.serializers import (
    CustomUserCreateListSerializer,
    CustomUserUpdateSerializer,
)

from vestgo_api.services.login_service import LoginService

from vestgo_api.services.user_service import UserService
from django.db.models import Q


class LoginView(TokenObtainPairView):
    def _build_dict_from_query_data(self, request: Request) -> dict:
        email = request.data.get("email")
        password = request.data.get("password")
        if not email or not password:
            raise ValidationError("Missing args.")

        return {"email": email, "password": password}

    def post(self, request, *args, **kwargs):
        try:
            credentials = self._build_dict_from_query_data(request)
            ret = LoginService.login(request, credentials)
            return Response(ret)
        except ValidationError as err:
            return Response({"error": str(err)}, status=status.HTTP_400_BAD_REQUEST)
        except AuthenticationFailed as err:
            return Response({"error": str(err)}, status=status.HTTP_401_UNAUTHORIZED)


class CustomUserCreateListView(generics.ListCreateAPIView):
    serializer_class = CustomUserCreateListSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get(self, request):
        return UserService().get_users_paginated(request)


class CustomUserRetrieveView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserCreateListSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]


class CustomUserUpdateView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserUpdateSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
