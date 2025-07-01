from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import get_object_or_404, redirect
from catalog.forms import ProductForm
from catalog.models import Category, Contact, Product


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
        return redirect('catalog:home')


class ProductsListViews(ListView):
    """
    Класс отвечающий за представление списка продукта.
    Отображает список продуктов в шаблоне home.html с пагинацией.
    Порядок отображения продуктов - от нового к старому (по полю updated_at)
    """

    model = Product
    template_name = "catalog/home.html"
    paginate_by = 4
    context_object_name = "products"

    def get_queryset(self):
        queryset = Product.objects.filter(publication="True").order_by("-updated_at")
        return queryset


class ContactsCreateView(CreateView):
    """
    Класс отвечающий за создание контактов.
    Позволяет пользователям отправлять свои контактные данные через форму, а также сохраняет их в модели Contact.
    После успешного создания перенаправляет на страницу контактов.
    """

    model = Contact
    template_name = "catalog/contacts.html"
    fields = ["name", "phone", "message"]
    success_url = reverse_lazy("catalog:contacts")


class ProductDetailViews(LoginRequiredMixin, DetailView):
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


class ProductCreateViews(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    Класс отвечающий за создание продукта.
    Позволяет пользователям добавлять новые продукты через форму.
    После успешного создания перенаправляет на главную страницу.
    Создание возможно только с правом add_product
    """

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")
    permission_required = 'catalog.add_product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class ProductUpdateViews(LoginRequiredMixin, UpdateView):
    """
    Класс отвечающий за изменения продукта.
    Позволяет пользователям редактировать продукты через форму.
    После успешного создания перенаправляет на детальную информацию о продукте.
    """

    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})


class ProductDeleteViews(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    Класс отвечающий за удаление продукта
    После успешного удаления перенаправляет на список блогов
    Удаление возможно только с правом delete_product
    """

    model = Product
    context_object_name = "product"
    success_url = reverse_lazy("catalog:home")
    permission_required = 'catalog.delete_product'
