from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from catalog.models import Product, Contact


def home(request: HttpRequest) -> HttpResponse:
    """
    Обрабатывает главную страницу
    :param request: Экземпляр HttpRequest.
    :return: HTML шаблон главной страницы
    """
    products = Product.objects.order_by('-created_at')[:5]
    for product in products:
        product_dict = {
            "name": product.name,
            "description": product.description,
            "image": product.image,
            "category": product.category.name, # product.category_id | product.category.name
            "price": product.price,
        }
        print(product_dict)
    return render(request,'catalog/home.html')


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

