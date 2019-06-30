from django.shortcuts import render, redirect
from django.views import generic

from .models import Book
from .forms import BookForm


class IndexView(generic.ListView):
    template_name = 'bookmgr/index.html'
    context_object_name = 'books'
    
    def get_queryset(self):
        return Book.objects.all()


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'bookmgr/detail.html'


def book_add(request):
    if request.method == 'POST':
        """Submit the book"""
        form = BookForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('bookmgr:index')

    return render(request, "bookmgr/add.html")


def book_delete_confirm(request, pk):
    return render(request, 'bookmgr/delete_confirm.html')
