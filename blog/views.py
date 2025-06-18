from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from blog.models import BlogPost


class BlogPostCreateView(CreateView):
    """
    Класс отвечающий за создание поста.
    После успешного создания блога переадресует на список блогов.
    """
    model = BlogPost
    fields = ["title", "content", "preview", "publication",]
    success_url = reverse_lazy("blog:blog_list")


class BlogPostDeleteViews(DeleteView):
    """
    Класс отвечающий за удаление поста.
    После успешного удаления пользователя перенаправляет на список блогов.
    """
    model = BlogPost
    context_object_name = 'blog'
    success_url = reverse_lazy("blog:blog_list")


class BlogPostDetailViews(DetailView):
    """
    Класс отвечающий за получение детальной информации о посте.
    При заходе пользователя на страницу, увеличивает количество просмотров.
    """
    model = BlogPost
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogsPostListViews(ListView):
    """
    Класс отвечающий за предоставление списка постов.
    Отображает список блогов в шаблоне blogpost_list.html с пагинацией.
    Отображения блогов - только опубликованные (publication=True)
    """
    model = BlogPost
    paginate_by = 4
    context_object_name = 'blogs'

    def get_queryset(self):
        queryset = BlogPost.objects.filter(publication=True)
        return queryset


class BlogPostUpdateViews(UpdateView):
    """
    Класс отвечающий за изменение поста.
    После удачного изменения переходит на детальную информацию о посте.
    """
    model = BlogPost
    fields = ["title", "content", "preview", "publication",]

    def get_success_url(self):
        return reverse_lazy("blog:blog_detail", kwargs={"pk": self.object.pk})
