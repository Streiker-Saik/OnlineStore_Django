from django.core.management import call_command
from django.core.management.base import BaseCommand

from blog.models import BlogPost


class Command(BaseCommand):
    """Команда для добавления продуктов из fixture"""

    help = "Add test blog post to the database"

    def handle(self, *args, **options) -> None:
        """Обрабатывает команду для добавления продуктов в базу данных"""
        # Удаляем все существующие категории и продукты
        BlogPost.objects.all().delete()

        call_command(
            "loaddata",
            (
                "blogpost_fixture.json",
            ),
        )
        self.stdout.write(self.style.SUCCESS("Успешно загружены данные из фикстуры"))
