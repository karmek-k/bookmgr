from django.shortcuts import render
from django.views import generic

from .models import Book


class IndexView(generic.ListView):
    template_name = 'bookmgr/index.html'
    context_object_name = 'books'
    
    def get_queryset(self):
        return Book.objects.all()


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'bookmgr/detail.html'


def book_add(request):
    return render(request, "bookmgr/add.html")