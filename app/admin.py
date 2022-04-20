from django.contrib import admin
from .models import Book, Genre, Author

class BookAdmin(admin.ModelAdmin):
  list_display  = ('title', 'author')
  search_fields = ('title',)

class AuthorAdmin(admin.ModelAdmin):
  list_display  = ('first_name', 'last_name')
  search_fields = ('first_name', 'last_name')

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)