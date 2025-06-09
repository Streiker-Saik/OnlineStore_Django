from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from catalog.models import Product, Contact


def home(request: HttpRequest) -> HttpResponse:
    """
    Обрабатывает главную страницу
    :param request: Экземпляр HttpRequest.
    :return: HTML шаблон главной страницы
    """
    products = Product.objects.all().order_by('-updated_at')
    context = {"products": products}
    return render(request,'catalog/home.html', context)


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
        Contact.objects.create(name=name, phone=phone, message=message)
        return HttpResponse(f"Спасибо {name}, сообщение принято.")

    return render(request, 'catalog/contacts.html')


def product_detail(request: HttpRequest, product_id: int) -> HttpResponse:
    """
    Обрабатывает страницу информации о продукте
    :param request: Экземпляр HttpRequest.
    :param product_id: ID продукта, (PrimaryKey)
    :return: HTML шаблон информации о продукте
    """
    product = Product.objects.get(pk=product_id)
    context = {'product': product}
    return render(request, 'catalog/product_detail.html', context)
