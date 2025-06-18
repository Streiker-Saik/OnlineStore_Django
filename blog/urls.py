from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.apps import BlogConfig

from .views import (
    BlogPostCreateView,
    BlogPostDeleteViews,
    BlogPostDetailViews,
    BlogsPostListViews,
    BlogPostUpdateViews,
)

app_name = BlogConfig.name

urlpatterns = [
    path("", BlogsPostListViews.as_view(), name="blog_list"),
    path("create/", BlogPostCreateView.as_view(), name="blog_create"),
    path("<int:pk>/detail/", BlogPostDetailViews.as_view(), name="blog_detail"),
    path("<int:pk>/delete/", BlogPostDeleteViews.as_view(), name="blog_delete"),
    path("<int:pk>/edit/", BlogPostUpdateViews.as_view(), name="blog_edit"),
]
