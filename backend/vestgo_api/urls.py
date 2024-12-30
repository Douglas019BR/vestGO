from django.urls import path

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from vestgo_api.views.custom_user_view import (
    LoginView,
    CustomUserCreateListView,
    CustomUserUpdateView,
    CustomUserRetrieveView,
)

urlpatterns = [
    path("login/", LoginView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("users/", CustomUserCreateListView.as_view()),
    path("users/<int:pk>/", CustomUserRetrieveView.as_view()),
    path("user/<int:pk>/", CustomUserUpdateView.as_view()),
]
