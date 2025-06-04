from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    """Команда для добавления тестовых продуктов"""
    help = "Add test products to the database"

    def handle(self, *args, **options) -> None:
        """Обрабатывает команду для добавления тестовых продуктов в базу данных"""
        # Удаляем все существующие категории и продукты
        Category.objects.all().delete()
        Product.objects.all().delete()

        call_command('loaddata', ('category_fixture.json', 'product_fixture.json',))
        self.stdout.write(self.style.SUCCESS('Успешно загружены данные из фикстуры'))
