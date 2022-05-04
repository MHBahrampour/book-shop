from django.urls import path
from . import views

urlpatterns = [

  # Home page
  path('', views.index, name='index'),

  path('shoppingCart', views.showShoppingCart, name='show_shopping_cart'),
  path('successfulPurchase', views.successfulPurchase, name='successful_purchase'),
  
  path('shoppingCart/<int:pk>/removeFromShoppingCart', views.removeFromShoppingCart, name='remove_from_shopping_cart'),

  path('books/', views.BookListView.as_view(), name='books'),
  path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
  path('book/<int:pk>/addToShoppingCart', views.addToShoppingCart, name='add_to_shopping_cart'),

  path('authors/', views.AuthorListView.as_view(), name='authors'),
  path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),

  path('genre/', views.GenreListView.as_view(), name='genre'),
  path('genre/<int:pk>', views.genreBooks, name='genre-books'),

  path("search/", views.SearchResultsView.as_view(), name="search-results"),
  
]
