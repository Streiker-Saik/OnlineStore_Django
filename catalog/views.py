from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


from catalog.models import Product, Contact, Category


def home(request: HttpRequest) -> HttpResponse:
    """
    Обрабатывает главную страницу. Со страницами по 4 продуктами
    :param request: Экземпляр HttpRequest.
    :return: HTML шаблон главной страницы
    """
    products = Product.objects.all().order_by('-updated_at')
    paginator = Paginator(products, 4)
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


def product_add(request: HttpRequest) -> HttpResponse:
    """
    Обрабатывает форму добавления продукта.
    Отправляет пользователю сообщение при успешной добавлении продукта.
    :param request: Экземпляр HttpRequest.
    :return: HTML страница при GET запросе или сообщение при успешном POST запросе
    """
    categories = Category.objects.all()
    context = {"categories": categories}
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        category_id = request.POST.get("category")
        price = request.POST.get("price")
        # if not all([name, price, category_id]):
        #     messages.error(request, "Пожалуйста, заполните все обязательные поля.")
        #     return render(request, 'catalog/product_add.html', context)
        Product.objects.create(name=name, description=description, image=image, category_id=category_id, price=price)
        return HttpResponse(f"Спасибо! Продукт {name}, добавлен.")

    return render(request, 'catalog/product_add.html', context)