from django.urls import path

from . import views


app_name = 'bookmgr'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>', views.BookDetailView.as_view(), name='detail'),
    path('add/', views.book_add, name="add")
]