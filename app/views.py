from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .models import Book, Author, Genre


def index(request):

  num_books = Book.objects.all().count()
  num_instances_available = Book.objects.filter(is_available__exact=True).count()
  num_authors = Author.objects.count()

  context = {
    'num_books': num_books,
    'num_instances_available': num_instances_available,
    'num_authors': num_authors,
  }

  return render(request, 'index.html', context)

class SearchResultsView(generic.ListView):
  model = Book
  template_name = 'app/search_results.html'

  def get_queryset(self):
    query = self.request.GET.get('query')
    return Book.objects.filter(title__icontains=query)


class BookListView(generic.ListView):
  model = Book
  paginate_by = 9

class BookDetailView(generic.DetailView):
  model = Book


class AuthorListView(generic.ListView):
  model = Author
  paginate_by = 9

class AuthorDetailView(generic.DetailView):
  model = Author


class GenreListView(generic.ListView):
  model = Genre
  paginate_by = 20

def genreBooks(request, pk):

  genre_books_list = Book.objects.filter(genre__pk=pk).select_related()
  for book in genre_books_list:
    print(book.author)

  context = {
    'this_genre': Genre.objects.get(pk=pk),
    'genre_books_list': genre_books_list,
  }

  return render(request, 'app/genre_books.html', context)


def addToCart(request, pk):

  return HttpResponse(f"Book with ID={pk}")


class Signup(generic.CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"