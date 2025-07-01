from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig

from .views import CustomLoginView, RegisterView, UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="catalog:home"), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("edit/", UserUpdateView.as_view(), name="edit"),
]
