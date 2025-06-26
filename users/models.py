from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Представление кастомного пользователя, расширяющее AbstractUser.
    Поле авторизации с username изменено на email.
    Так же username обязательное поле при авторизации
    Атрибуты:
        avatar(ImageField): Аватар (изображение)
        phone_number(str): Номер телефона
        country(str): Страна
    """

    avatar = models.ImageField("avatars/", blank=True, null=True, verbose_name="Аватар")
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Номер телефона")
    country = models.CharField(max_length=65, blank=True, null=True, verbose_name="Страна")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        """
        Строковое представление класса.
        :return: Электронная почта
        """
        return self.email
