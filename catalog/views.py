from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Category, Contact, Product


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
        queryset = Product.objects.all().order_by("-updated_at")
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


class ProductDetailViews(DetailView):
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


class ProductCreateViews(CreateView):
    """
    Класс отвечающий за создание продукта.
    Позволяет пользователям добавлять новые продукты через форму.
    После успешного создания перенаправляет на главную страницу.
    """

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class ProductUpdateViews(UpdateView):
    """
    Класс отвечающий за изменения продукта.
    Позволяет пользователям редактировать продукты через форму.
    После успешного создания перенаправляет на детальную информацию о продукте.
    """

    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})


class ProductDeleteViews(DeleteView):
    """
    Класс отвечающий за удаление продукта
    После успешного удаления перенаправляет на список блогов.
    """

    model = Product
    context_object_name = "product"
    success_url = reverse_lazy("catalog:home")
