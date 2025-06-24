from django import forms
from django.core.exceptions import ValidationError

from .models import Product

FORBIDDEN_WORDS = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]


class ProductForm(forms.ModelForm):
    """
    Форма для создания и редактирования продукта.
    Включает в себя валидацию, которая запрещает использование определенных слов в name и description
    """

    class Meta:
        model = Product
        fields = "__all__"

    def clean(self) -> dict:
        """
        Валидация полей формы.
        Проверяет поля name и description на наличие запрещенных слов
        :return: Данные формы
        :raise ValidationError: При нахождении запрещенных слов.
        """
        clean_data = super().clean()
        name = clean_data.get('name')
        description = clean_data.get('description')
        errors = []

        for word in FORBIDDEN_WORDS:
            if word in name.lower():
                errors.append(f'Название не должно содержать слова: {word}')
            if word in description.lower():
                errors.append(f'Описание не должно содержать слова: {word}')

        if errors:
            raise ValidationError(errors)

        return clean_data
