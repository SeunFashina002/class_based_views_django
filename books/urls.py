from unicodedata import name
from django.urls import path
from .views import HomePage, GenreView, BookDetails, CreateBook, UpdateBook
from django.views.generic.base import TemplateView

app_name = 'bookstore'
urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('add-book/', CreateBook.as_view(), name='create-book'),
    path('edit/<slug:slug>/', UpdateBook.as_view(), name='update-book'),
    path('error/', TemplateView.as_view(template_name='error.html')),
    path('genre/<str:g>/', GenreView.as_view(), name='genre'),
    path('<slug:slug>/', BookDetails.as_view(), name='details'),
]