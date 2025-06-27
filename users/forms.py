from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import CustomUser

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    """
    Кастомная форма регистрации пользователя.
    Атрибуты:
        username(str): Логин пользователя, обязательный параметр
        usable_password: Устанавливает параметр для управления паролем
    Методы:
        __init__: Инициализирует поля формы с пользовательскими настройками и атрибутами.
    """

    username = forms.CharField(max_length=50, required=True)
    usable_password = None

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("email", "username", "password1", "password2")

    def __init__(self, *args, **kwargs) -> None:
        """Инициализирует поля формы с пользовательскими настройками"""
        super().__init__(*args, **kwargs)
        self.fields["email"].label = "Электронная почта"
        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите адрес электронной почты"}
        )

        self.fields["username"].label = "Логин"
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите уникальный логин"}
        )

        self.fields["password1"].label = "Пароль"
        self.fields["password1"].widget.attrs.update({"class": "form-control", "placeholder": "Введите пароль"})
        self.fields["password1"].help_text = (
            "<ul>"
            "<li>Ваш пароль не может быть слишком похож на другую личную информацию.</li>"
            "<li>Пароль должен содержать не менее 8 символов.</li>"
            "<li>Пароль не может быть слишком распространенным.</li>"
            "<li>Пароль не может состоять только из цифр.</li>"
            "</ul>"
        )

        self.fields["password2"].label = "Подтверждение пароля"
        self.fields["password2"].widget.attrs.update({"class": "form-control", "placeholder": "Введите тот же пароль"})
        self.fields["password2"].help_text = "Введите тот же пароль, что и выше, для проверки."


class CustomAuthenticationForm(AuthenticationForm):
    """
    Кастомная форма авторизации пользователя
    Методы:
        __init__ -> None
            Инициализирует поля формы с пользовательскими настройками и атрибутами
        clean_username -> str
            Проверка наличие пользователя с указанным адресом электронной почты
            :raise ValidationError: Если пользователь не зарегистрирован.
    """

    def __init__(self, *args, **kwargs) -> None:
        """Инициализирует поля формы с пользовательскими настройками"""
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Электронная почта"
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите адрес электронной почты"}
        )
        self.fields["password"].label = "Пароль"
        self.fields["password"].widget.attrs.update({"class": "form-control", "placeholder": "Введите пароль"})

    def clean_username(self) -> str:
        """
        Проверка наличие пользователя с указанным адресом электронной почты.
        :return: Возвращает почту
        :raise ValidationError: Если пользователь не зарегистрирован.
        """
        email = self.cleaned_data.get("username")
        try:
            user = User.objects.get(email=email)
            return user.email

        except User.DoesNotExist:
            raise forms.ValidationError("Пользователь с такой электронной почтой не найден")
