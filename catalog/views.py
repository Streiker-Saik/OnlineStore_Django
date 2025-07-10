from typing import Optional

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, View, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from catalog.forms import ProductForm
from catalog.models import Category, Contact, Product

from .services import DecoratorsService, ProductService, CategoryService

cache_decorator = DecoratorsService.get_cache_decorator()


class BaseView(View):
    """
    Базовое представление для добавления общей информации в контекст представлений.
    Метод:
        get_context_data(self, **kwargs) -> dict:
            Добавляем в контекст все категории
    """

    def get_context_data(self, **kwargs) -> dict:
        """Добавляем в контекст все категории"""
        context = {}
        categories = CategoryService.get_all_categories()
        context['categories'] = categories
        return context


class PublishProductViews(LoginRequiredMixin, View):
    """
    Представление отвечающее за снятие публикации продукта.
    Снять с публикации возможно с правом can_unpublish_product
    """

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if not request.user.has_perm("catalog.can_unpublish_product"):
            return HttpResponse("У вас нет прав отменить публикацию")
        product.publication = False
        product.save()
        return redirect("catalog:home")


class ProductsListViews(BaseView, ListView):
    """
    Класс отвечающий за представление списка продукта.
    Отображает список продуктов в шаблоне home.html с пагинацией.
    Порядок отображения продуктов - от нового к старому (по полю updated_at)
    """

    model = Product
    template_name = "catalog/home.html"
    paginate_by = 4
    context_object_name = "products"
    ordering = ["-updated_at"]

    def get_queryset(self) -> QuerySet:
        """
        Переопределение метода get_queryset для получения списка продуктов.
        Если у пользователя есть права на закрытие публикации, он видит все продукты.
        Если прав нет, он видит только опубликованные продукты.
        :return: QuerySet продуктов, отсортированных по дате обновления в порядке убывания.
        """
        user = self.request.user
        products = ProductService.get_products_from_cache()
        products = ProductService.filter_products_by_permission(products, user)
        return products



class ProductsByCategoryListViews(BaseView, ListView):
    """
    Класс отвечающий за предоставление продуктов в категории.
    Отображает список продуктов в шаблоне products_by_category.html с пагинацией.
    Категория добавляется в контекст.
    Порядок отображения продуктов - от нового к старому (по полю updated_at).
    """

    model = Product
    template_name = "catalog/products_by_category.html"
    paginate_by = 4
    context_object_name = "products"

    def get_queryset(self) -> QuerySet:
        """
        Переопределение метода get_queryset для получения списка продуктов по категории.
        Если у пользователя есть права на закрытие публикации, он видит все продукты.
        Если прав нет, он видит только опубликованные продукты.
        :return: QuerySet продуктов по категории, отсортированных по дате обновления в порядке убывания.
        """
        category_id = self.kwargs["pk"]
        user = self.request.user
        products = ProductService.get_products_by_category(category_id)
        products = ProductService.filter_products_by_permission(products, user)
        return products

    def get_context_data(self, **kwargs):
        """Добавляем в контекст текущую категорию"""
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, pk=self.kwargs["pk"])
        context["category"] = category
        return context


class ContactsCreateView(BaseView, CreateView):
    """
    Класс отвечающий за создание контактов.
    Позволяет пользователям отправлять свои контактные данные через форму, а также сохраняет их в модели Contact.
    После успешного создания перенаправляет на страницу контактов.
    """

    model = Contact
    template_name = "catalog/contacts.html"
    fields = ["name", "phone", "message"]
    success_url = reverse_lazy("catalog:contacts")


@cache_decorator
class ProductDetailViews(LoginRequiredMixin, BaseView, DetailView):
    """
    Класс отвечающий за получение детальной информации о продукте.
    Отображает полные данные о выбранном продукте в шаблоне product_detail.html.
    Добавляет информацию о категории продукта в контекст.
    """

    model = Product
    template_name = "catalog/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        context["category"] = product.category
        return context


class ProductCreateViews(LoginRequiredMixin, BaseView, CreateView):
    """
    Класс отвечающий за создание продукта.
    Позволяет пользователям добавлять новые продукты через форму.
    После успешного создания перенаправляет на главную страницу.
    Создание возможно только с правом add_product
    Автоматически указывает владельца продукта
    """

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    # permission_required = "catalog.add_product" PermissionRequiredMixin,


    def form_valid(self, form):
        """
        Обрабатывает форму, если она является действительной.
        Устанавливает владельца на текущего пользователя.
        """

        product = form.save(commit=False)
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateViews(LoginRequiredMixin, BaseView, UpdateView):
    """
    Класс отвечающий за изменения продукта.
    Позволяет пользователям редактировать продукты через форму.
    После успешного создания перенаправляет на детальную информацию о продукте.
    Только создатель или пользователь с наличием прав может изменить продукт.
    """

    model = Product
    form_class = ProductForm

    def dispatch(self, request, *args, **kwargs):
        """
        Проверка доступа пользователя к редактированию продукта.
        """
        product = self.get_object()
        user = self.request.user
        if not (product.owner == user or user.has_perm("catalog.create_product")):
            return HttpResponseForbidden("У вас нет прав на редактирование этого продукта.")
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})


class ProductDeleteViews(LoginRequiredMixin, BaseView, DeleteView):
    """
    Класс отвечающий за удаление продукта
    После успешного удаления перенаправляет на список блогов
    Удаление возможно только с правом delete_product
    Только создатель или пользователь с наличием прав может удалить продукт.
    """

    model = Product
    context_object_name = "product"
    success_url = reverse_lazy("catalog:home")

    # permission_required = "catalog.delete_product" PermissionRequiredMixin,

    def dispatch(self, request, *args, **kwargs):
        """Проверка, что у пользователя есть доступ к удалению продукта"""
        product = self.get_object()
        user = self.request.user
        if not (user == product.owner or user.has_perm("catalog.delete_product")):
            return HttpResponseForbidden("У вас нет прав удалить продукт")
        return super().dispatch(request, *args, **kwargs)


class CategoryListViews(BaseView, ListView):
    """
    Класс отвечающий за представление списка категорий.
    Отображает список продуктов в шаблоне categories_list.html.
    Порядок отображения категорий - по алфавиту (по полю name)
    """

    model = Category
    template_name = "catalog/categories_list.html"
    ordering = ["name"]
    context_object_name = "categories"
