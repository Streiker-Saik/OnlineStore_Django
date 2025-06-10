from django.core.paginator import Paginator
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
    paginator = Paginator(products, 1)
    page_number = request.GET.get('page') # получаем номер страницы
    products = paginator.get_page(page_number)
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


def product_detail(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Обрабатывает страницу информации о продукте
    :param request: Экземпляр HttpRequest.
    :param pk: ID продукта (PrimaryKey)
    :return: HTML шаблон информации о продукте
    """
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'catalog/product_detail.html', context)
