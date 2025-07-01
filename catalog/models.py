from django.db import models


class Category(models.Model):
    """
    Модель представляющая категорию

    Атрибуты:
        name(str): Название категории
        description(str): Описание категории
    """

    name: str = models.CharField(max_length=150, verbose_name="Наименование")
    description: str = models.TextField(verbose_name="Описание", blank=True, null=True)

    def __str__(self) -> str:
        """
        Строковое представление продуктов
        :return: Наименование категории
        """
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]


class Product(models.Model):
    """
    Модель, представляющая продукт
    Атрибуты:
        name(str): Наименование продукта
        description(str): Описание продукта
        image(ImageField): Изображение продукта
        category(ForeignKey): Связь с категорией, к которой принадлежит продукт
        price(float): Цена продукта
        created_at(datetime): Дата и время создания продукта
        updated_at(datetime): Дата и время последнего изменения продукта
        publication(bool): Публикация продукта
    """

    name: str = models.CharField(max_length=150, verbose_name="Наименование")
    description: str = models.TextField(verbose_name="Описание", blank=True, null=True)
    image = models.ImageField(upload_to="images/", verbose_name="Изображение", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category", verbose_name="Категория")
    price: float = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    publication = models.BooleanField(verbose_name="Публиковано", default=False)

    def __str__(self) -> str:
        """
        Строковое представление продуктов
        :return: Наименование категории
        """
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]


class Contact(models.Model):
    """
    Модель, предоставления контактных данных
    """

    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self) -> str:
        """
        Строковое представление контактных данных
        :return: Наименование категории
        """
        return f"{self.name}: {self.phone}"

    class Meta:
        verbose_name = "контакт"
        verbose_name_plural = "контакты"
        ordering = ["name"]
