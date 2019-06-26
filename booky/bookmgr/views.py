from django.shortcuts import render
from django.views import generic

from .models import Book


class IndexView(generic.ListView):
    template_name = 'bookmgr/index.html'
    queryset = Book.objects.all()
