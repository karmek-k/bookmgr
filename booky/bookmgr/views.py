from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy

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


class BookDeleteView(generic.DeleteView):
    template_name = 'bookmgr/delete.html'
    model = Book
    success_url = reverse_lazy('bookmgr:index')


def book_edit(request, pk):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(request.POST or None, instance=book)
        if form.is_valid():
            form.save()
        return redirect('bookmgr:index')
    
    return render(request, 'bookmgr/edit.html', {'pk': pk})