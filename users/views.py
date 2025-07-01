from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import CustomAuthenticationForm, CustomUserCreationForm, UserUpdateForm


class RegisterView(CreateView):
    """
    Кастомное представление регистрации пользователя
    При успешной валидации отправляет приветственное письмо пользователю
    Методы:
        form_valid(self, form) -> HttpResponse:
            Обрабатывает валидную форму и выполняет дополнительное действие
        send_welcome_email(self, user_email: str) -> None:
            Отправляет приветственное письмо пользователю
    """

    template_name = "users/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form) -> HttpResponse:
        """Обрабатывает валидную форму и выполняет дополнительное действие"""
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email: str) -> None:
        """
        Отправляет приветственное письмо пользователю
        :param user_email: Электронная почта пользователя для отправки письма.
        """
        subject = "Добро пожаловать в наш сервис"
        message = "Спасибо, что зарегистрировались в нашем сервисе!"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)


class CustomLoginView(LoginView):
    """Кастомное представление регистрации пользователя"""

    template_name = "users/login.html"
    form_class = CustomAuthenticationForm
    success_url = reverse_lazy("catalog:home")


class UserUpdateView(UpdateView):
    template_name = "users/register.html"
    form_class = UserUpdateForm
    success_url = reverse_lazy("catalog:home")

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
