from django.contrib.auth import authenticate
from requests import Request
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import RefreshToken


class CustomToken(RefreshToken):
    @classmethod
    def for_user(cls, user):
        token = super().for_user(user)

        return token


class LoginService:
    @staticmethod
    def login(request: Request, credentials: dict) -> dict:
        user = authenticate(
            request, email=credentials["email"], password=credentials["password"]
        )
        if not user:
            raise AuthenticationFailed("Login or Password incorrect.")

        refresh = CustomToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "name": user.name,
            "email": user.email,
            "is_staff": user.is_staff,
            "groups": [g.name for g in user.groups.all()],
        }
