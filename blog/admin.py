from django.contrib import admin

from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """Класс для работы администратора с категориями"""

    list_display = ("id", "title", "content", "publication", "views_count")
    list_filter = (
        "publication",
        "views_count",
    )
    search_fields = (
        "title",
        "content",
    )
    ordering = ("created_at",)
