from django.utils import timezone
from django.db.models import F
# from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import  CreateView, UpdateView
from .models import Books
# from django.shortcuts import redirect, render
from django.contrib.auth.mixins import PermissionRequiredMixin
from .mixins import UserAccessMixin
from .forms import BookAddForm
# Create your views here.


class HomePage(ListView):
    model = Books
    template_name = 'index.html'
    context_object_name = 'books'

class GenreView(ListView):
    model = Books
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Books.objects.filter(genre__icontains=self.kwargs['g'])

        return context


class BookDetails(DetailView):    
    template_name = 'book-detail.html'
    model = Books
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        post = Books.objects.get(slug=self.kwargs['slug'])
        post.count = F('count')+1
        post.save()
        context['time'] = timezone.now()
        return context


class CreateBook(UserAccessMixin, CreateView):
    permission_required = 'books.add_books'
    login_url = '/' # this is wrong. Yeah, but its just for testing purposes
    model = Books
    template_name = 'forms/book-create.html'
    form_class = BookAddForm
    success_url = '/'

class UpdateBook(UserAccessMixin, UpdateView):
    permission_required ='books.change_books'
    redirect_field_name ='next'
    raise_exception = False
    login_url = '/' # this is wrong. Yeah, but its just for testing purposes
    model = Books
    template_name = 'forms/book-create.html'
    form_class = BookAddForm
    success_url = '/'


# other methods for the same stuff above

"""
TemplateView in place of ListView

class HomePage(TemplateView):
    template_name = 'index.html'
    
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['books'] = Books.objects.all()
        return context


function based view in place of hompage list view

def homepage(request):
    books = Books.objects.all()
    context ={
        'books':books
    }

    return render(request, 'index.html', context)


function based view for the GenreView

def categorize(request, **kwargs):
    books = Books.objects.filter(genre__icontains=kwargs['g'])
    print(books)
    context = {
        'books' : books,
    } 

    return render(request, 'index.html', context)
    
function based view for Book Details


def bookDetails(request, slug):
    book = Books.objects.get(slug=slug)
    book.count +=1
    book.save()
    time = timezone.now()
    context = {
        'book':book,
        'time':time,
    }

    return render(request, 'book-detail.html', context)

form view

class CreateBook(FormView):
    template_name = 'forms/book-create.html'
    form_class = BookAddForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

create view

def createBook(request):
    form = BookAddForm()
    if request.method == 'POST':
        form = BookAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = BookAddForm()
    context = {
        'form' : form,
    }

    return render(request, 'forms/book-create.html', context)




update view 

def updateBook(request, slug):
    book = Books.objects.get(slug=slug)
    form = BookAddForm(instance=book)

    if request.method == 'POST':
        form = BookAddForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = BookAddForm()
    context = {
        'form':form,
    }
    return render(request, 'forms/book-create.html', context)




"""