from django.core.management import call_command
from django.core.management.base import BaseCommand

from django.contrib.auth.models import Group


class Command(BaseCommand):
    """Команда для добавления продуктов из fixture"""

    help = "Add test group to the database"

    def handle(self, *args, **options) -> None:
        """Обрабатывает команду для добавления продуктов в базу данных"""
        # Удаляем все существующие категории и продукты
        Group.objects.all().delete()

        call_command(
            "loaddata",
            (
                "group_fixture.json.json",
            ),
        )
        self.stdout.write(self.style.SUCCESS("Успешно загружены данные из фикстуры"))
