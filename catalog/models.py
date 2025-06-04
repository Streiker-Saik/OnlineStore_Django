from django.db import models


class Category(models.Model):
    """
    Модель представляющая категорию

    Атрибуты:
        name(str): Название категории
        description(str): Описание категории
    """

    name: str = models.CharField(max_length=150, verbose_name="Наименование")
    description: str = models.CharField(max_length=250, verbose_name="Описание")

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
    """

    name: str = models.CharField(max_length=150, verbose_name="Наименование")
    description: str = models.CharField(max_length=150, verbose_name="Описание")
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    price: float = models.FloatField(verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

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
