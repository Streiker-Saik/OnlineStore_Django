from django.db import models

class BlogPost(models.Model):
    """
    Модель представляет записи блога
    Атрибуты:
        title(str): Заголовок
        content(str): Содержание
        preview(ImageField): Превью(изображение)
        created_at(datetime): Дата и время создания продукта
        publication(bool): Признак публикации
        views_count(int): Количество просмотров
    """
    title: str  = models.CharField(max_length=150, verbose_name="Заголовок")
    content: str = models.TextField(verbose_name="Содержание")
    preview = models.ImageField(upload_to='preview/', verbose_name='Изображение', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    publication = models.BooleanField(verbose_name="Публиковано", default=False)
    views_count = models.PositiveIntegerField(verbose_name="Количество просмотров", default=0)

    def __str__(self) -> str:
        """
        Строковое представление продуктов
        :return: Наименование категории
        """
        return self.title

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"
        ordering = ["created_at"]
