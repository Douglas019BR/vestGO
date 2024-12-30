from rest_framework.request import Request
from rest_framework.response import Response


from vestgo_api.models import CustomUser
from vestgo_api.serializers import CustomUserCreateListSerializer
from vestgo_api.services.paginate import paginate


class UserService:
    def get_users_paginated(self, request: Request) -> Response:
        query_set = CustomUser.objects
        return paginate(query_set, request, CustomUserCreateListSerializer)
