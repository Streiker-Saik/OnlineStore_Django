from django import forms
from django.core.exceptions import ValidationError
from django.db.models.fields.files import ImageFieldFile

from .models import Product

FORBIDDEN_WORDS = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]


class ProductForm(forms.ModelForm):
    """
    Форма для создания и редактирования продукта.
    Включает в себя валидации:
        запрещает использование определенных слов в name и description
        запрещает цене быть отрицательной
        запрещает загружать файлы не форматов JPG/PNG и с размером больше 5 МБ
    """

    class Meta:
        model = Product
        exclude = ['publication', 'owner',]

    def __init__(self, *args, **kwargs):
        """Инициализация стилизации форм"""
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control", "placeholder": "Введите название продукта"})
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание продукта"}
        )
        self.fields["image"].widget.attrs.update({"class": "btn btn-outline-secondary"})
        self.fields["category"].widget.attrs.update({"class": "form-select"})
        self.fields["price"].widget.attrs.update({"class": "form-control", "placeholder": "Введите цену продукта"})

    def clean(self) -> dict:
        """
        Валидация полей формы.
        Проверяет поля name и description на наличие запрещенных слов
        :return: Данные формы
        :raise ValidationError: При нахождении запрещенных слов.
        """
        clean_data = super().clean()
        name = clean_data.get("name")
        description = clean_data.get("description")
        errors = []

        for word in FORBIDDEN_WORDS:
            if word in name.lower():
                errors.append(f"Название не должно содержать слова: {word}")
            if word in description.lower():
                errors.append(f"Описание не должно содержать слова: {word}")

        if errors:
            raise ValidationError(errors)

        return clean_data

    def clean_price(self) -> float:
        """
        Валидация цены
        :return: Валидация прошла успешно, возвращает цену.
        :raise ValidationError: При отрицательной цене.
        """
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена не может быть меньше 0")
        return price

    def clean_image(self) -> "ImageFieldFile":
        """
        Валидация изображения
        Проверка расширения и размера
        :return: Загруженное изображение
        :raise ValidationError: Файл не форматов JPG/PNG или превышает 5 МБ
        """
        image = self.cleaned_data.get("image")
        if not (image.name.endswith("png") or image.name.endswith("jpg") or image.name.endswith("jpeg")):
            raise ValidationError("Файл должен быть форма JPG/PNG")
        if image.size > 5 * 1024 * 1024:
            raise ValidationError("Файл не должен превышать 5 МБ")
        return image
