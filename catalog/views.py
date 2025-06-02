from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    """
    Обрабатывает главную страницу
    :param request: Экземпляр HttpRequest.
    :return: HTML шаблон главной страницы
    """
    return render(request, 'catalog/home.html')


def contacts(request: HttpRequest) -> HttpResponse:
    """
    Обрабатывает контактную форму.
    Отправляет пользователю сообщение при успешной отправке.
    :param request: Экземпляр HttpRequest.
    :return: HTML страница при GET запросе или сообщение при успешном POST запросе
    """
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name}({phone}): {message}")
        return HttpResponse(f"Спасибо {name}, сообщение принято.")

    return render(request, 'catalog/contacts.html')
