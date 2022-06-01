from django.db import models
from django.urls import reverse
from django.conf import settings


class Genre(models.Model):
  """Model representing a book genre."""

  name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

  def __str__(self):
    """String for representing the Model object."""
    return self.name

  def get_absolute_url(self):
    """Returns the URL to access a list of books in a specific genre."""
    return reverse('genre-books', args=[str(self.id)])


class Author(models.Model):
  """Model representing an author."""

  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)

  date_of_birth = models.DateField()
  date_of_death = models.DateField(null=True)

  biography = models.TextField(max_length=1000, help_text='Enter a brief biography of the author')

  portrait = models.ImageField(upload_to='portraits/', default='defaultPortrait.jpg')

  def __str__(self):
    """String for representing the Model object."""
    return f'{self.first_name} {self.last_name}'

  def get_absolute_url(self):
    """Returns the URL to access a particular author instance."""
    return reverse('author-detail', args=[str(self.id)])


class Book(models.Model):
  """Model representing a book (but not a specific copy of a book)."""

  title = models.CharField(max_length=200)

  # Foreign Key used because book can only have one author, but authors can have multiple books
  author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

  summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
  isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='13 Character ISBN number')

  cover = models.ImageField(upload_to='covers/', default='defaultCover.jpg')

  # ManyToManyField used because genre can contain many books. Books can cover many genres.
  genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

  price = models.CharField(max_length=3, default='N/A', help_text='Price in US Dollar')

  is_available = models.BooleanField(default=True)

  def __str__(self):
    """String for representing the Model object."""
    return self.title

  def get_absolute_url(self):
    """Returns the URL to access a detail record for this book."""
    return reverse('book-detail', args=[str(self.id)])


class ShoppingCart(models.Model):

  # The link between User and ShoppingCart
  user  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  # All the books inside the user Shopping Cart
  books = models.ManyToManyField(Book)

  def __str__(self):
    return self.user.username


class Comment(models.Model):

  SCORE_CHOICES = [
    ('1', "1"),
    ('2', "2"),
    ('3', "3"),
    ('4', "4"),
    ('5', "5"),
  ]

  RECOMMEND_CHOICES = [
    ('I Dont Recommend It', "I Dont Recommend It"),
    ('Not Sure To Recommend', "Not Sure To Recommend"),
    ('I Recommend It', "I Recommend It"),
  ]

  user      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  book      = models.ForeignKey(Book, on_delete=models.CASCADE)

  score     = models.CharField(max_length=1, choices=SCORE_CHOICES)

  recommend = models.CharField(max_length=50, choices=RECOMMEND_CHOICES)

  text      = models.TextField(max_length=1000)

  date_time = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    """String for representing the Model object."""
    return self.user.username

  def get_absolute_url(self):
    """Returns the URL to access a list of books in a specific genre."""
    return reverse('genre-books', args=[str(self.id)])