from django.contrib import admin
from .models import all_book, book, author, book_authors, book_bookshelves, book_languages, book_subjects, bookshelf, format, language, subject
# Register your models here.
admin.site.register(all_book)
admin.site.register(book)
admin.site.register(author)
admin.site.register(book_authors)
admin.site.register(book_bookshelves)
admin.site.register(book_languages)
admin.site.register(book_subjects)
admin.site.register(bookshelf)
admin.site.register(format)
admin.site.register(language)
admin.site.register(subject)