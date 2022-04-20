from django.urls import path
from . import views

urlpatterns = [

  # Home page
  path('', views.index, name='index'),

  path('books/', views.BookListView.as_view(), name='books'),
  path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),

  path('author/', views.AuthorListView.as_view(), name='author'),
  path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),

  path('genre/', views.GenreListView.as_view(), name='genre'),
  path('genre/<int:pk>', views.genreBooks, name='genre-books'),

  #path('profile/', views.profile, name='profile'),
]
