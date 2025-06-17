from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class BlogCreateView(CreateView):
    """Класс отвечающий за создание"""
    pass


class BlogDeleteViews(DeleteView):
    """Класс отвечающий за удаление"""
    pass


class BlogDetailViews(DetailView):
    """Класс отвечающий за получение детальной информации"""
    pass


class BlogsListViews(ListView):
    """Класс отвечающий за предоставление списка блогов"""
    pass


class BlogUpdateViews(UpdateView):
    """Класс отвечающий за изменение блога"""
    pass
