from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [

  # Home page
  path('', RedirectView.as_view(pattern_name='books', permanent=True)),

  path('shoppingCart/', views.showShoppingCart, name='show_shopping_cart'),
  path('successfulPurchase/', views.successfulPurchase, name='successful_purchase'),
  
  path('shoppingCart/<int:pk>/removeFromShoppingCart/', views.removeFromShoppingCart, name='remove_from_shopping_cart'),

  path('books/', views.BookListView.as_view(), name='books'),
  path('book/<int:pk>/', views.bookDetail, name='book-detail'),
  path('book/<int:pk>/addToShoppingCart/', views.addToShoppingCart, name='add_to_shopping_cart'),

  path('authors/', views.AuthorListView.as_view(), name='authors'),
  path('author/<int:pk>/', views.authorDetail, name='author-detail'),

  path('genres/', views.GenreListView.as_view(), name='genres'),
  path('genre/<int:pk>/', views.genreBooks, name='genre-books'),

  path("search/", views.SearchResultsView.as_view(), name="search"),

  path("contact/", views.contact, name="contact"),
  path("contact/successful", views.successfulContact, name="successful_contact"),
  
]
