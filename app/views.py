import imp
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .models import Book, Comment, Author, Genre, ShoppingCart
from .forms import CommentForm


class SearchResultsView(generic.ListView):
  model = Book
  template_name = 'app/search_results.html'

  def get_queryset(self):
    query = self.request.GET.get('query')
    return Book.objects.filter(title__icontains=query)


class BookListView(generic.ListView):
  model = Book
  paginate_by = 9  


def bookDetail(request, pk):

  # Define context dictionary to be filled in the process
  context = {}

  # Get User model of the current user 
  user = request.user

  # Get the book detail and a list of all books in that genre
  book = Book.objects.get(pk=pk)
  first_genre_id = book.genre.first().id
  genre_books_list = Book.objects.filter(genre__pk=first_genre_id).select_related().exclude(pk=pk)
  
  context['book'] = book
  context['genre_books_list'] = genre_books_list

  # If the request type is POST
  if request.POST:

    # Create the respective Form with a POST request
    form = CommentForm(request.POST)

    # Check if the form passed verifications
    if form.is_valid():

      # Create and save the Comment instance
      Comment.objects.create(
        user    = user,
        book    = book,
        score   = form.cleaned_data.get('score'),
        recommend = form.cleaned_data.get('recommend'),
        text = form.cleaned_data.get('text'),
      )

      # Redirect user to the TransactionDetail page
      return redirect('book-detail', pk=book.id)

    # If form wasn't valid, return unvalid form to be filled again
    else:
      context['comment_form'] = form

  # If the request type is GET, create an empty form and pass it to template
  else:
    form = CommentForm()
    context['comment_form'] = form

  # Get all comments for this book
  comments = Comment.objects.filter(book__pk=book.id).select_related().order_by('-date_time')
  context['comments'] = comments
  
  return render(request, 'app/book_detail.html', context)


class AuthorListView(generic.ListView):
  model = Author
  paginate_by = 9


def authorDetail(request, pk):
  author = Author.objects.get(pk=pk)
  author_books_list = Book.objects.filter(author__pk=pk).select_related()
  
  context = {
    'author': author,
    'author_books_list': author_books_list,
  }
  
  return render(request, 'app/author_detail.html', context)


class GenreListView(generic.ListView):
  model = Genre
  paginate_by = 20

def genreBooks(request, pk):

  genre_books_list = Book.objects.filter(genre__pk=pk).select_related()

  context = {
    'this_genre': Genre.objects.get(pk=pk),
    'genre_books_list': genre_books_list,
  }

  return render(request, 'app/genre_books.html', context)


def showShoppingCart(request):

  if not request.user.is_authenticated:
    return redirect('books')

  shopping_cart = ShoppingCart.objects.get(user=request.user)
  number_of_books = shopping_cart.books.all().count()

  context = {}
  if number_of_books > 0:

    total_price = 0
    for book in shopping_cart.books.all():
      total_price += int(book.price)

    context = {
      'shopping_cart': shopping_cart,
      'number_of_books': number_of_books,
      'total_price': total_price,
    }

  return render(request, 'app/shopping_cart.html', context)

def addToShoppingCart(request, pk):

  book = Book.objects.get(pk=pk)

  if not request.user.is_authenticated:
    context = { 'pk': pk }
    return render(request, 'app/login_first.html', context)
    
  # Check if the User has a ShoppingCart instance
  try:
    shopping_cart = ShoppingCart.objects.get(user=request.user)

  # If he/she hasn't
  except ShoppingCart.DoesNotExist:
    shopping_cart = ShoppingCart()
    shopping_cart.user = request.user
    shopping_cart.save()
    shopping_cart.books.add(book)

  # If he/she has
  else:
    shopping_cart.books.add(book)
    
  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def removeFromShoppingCart(request, pk):

  book = Book.objects.get(pk=pk)

  shopping_cart = ShoppingCart.objects.get(user=request.user)
  shopping_cart.books.remove(book)

  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def successfulPurchase(request):

  shopping_cart = ShoppingCart.objects.get(user=request.user)

  for book in shopping_cart.books.all():
    shopping_cart.books.remove(book)

  return render(request, 'app/successful_purchase.html')


class Signup(generic.CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"