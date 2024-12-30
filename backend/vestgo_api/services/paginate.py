from typing import Any, Type
from rest_framework.pagination import PageNumberPagination
from rest_framework.settings import api_settings
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import BaseSerializer
from django.db.models import QuerySet


def paginate(
    query_set: QuerySet,
    request: Request,
    serializer_class: Type[BaseSerializer],
    use_all: bool = True,
    page_size: int = None,
) -> Response:
    templates = query_set.all() if use_all else query_set
    paginator = PageNumberPagination()
    if page_size:
        paginator.page_size = page_size
    else:
        paginator.page_size = api_settings.PAGE_SIZE
    result_page = paginator.paginate_queryset(templates, request)
    serialized_data = serializer_class(result_page, many=True)
    return paginator.get_paginated_response(serialized_data.data)
