from django.db import models

# Create your models here.
class all_book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    genre = models.CharField(max_length=1000)
    language = models.CharField(max_length=50)
    bookshelves = models.CharField(max_length=1000)
    subjects = models.TextField()
    download_links = models.TextField()
    mime_type = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class book(models.Model):
    id = models.IntegerField(primary_key=True)
    download_count = models.IntegerField()
    gutenberg_id = models.IntegerField()
    media_type = models.CharField(max_length=16)
    title = models.TextField()

    def __str__(self):
        return self.title

class author(models.Model):
    id = models.IntegerField(primary_key=True)
    birth_year = models.SmallIntegerField(null=True)
    death_year = models.SmallIntegerField(null=True)
    name = models.CharField(max_length=16)
    
    def __str__(self):
        return self.name

class book_authors(models.Model):
    id = models.IntegerField(primary_key=True)
    book_id = models.IntegerField()
    author_id = models.IntegerField()
    
    def __str__(self):
        return 'Author Id: '+str(self.author_id)

class book_bookshelves(models.Model):
    id = models.IntegerField(primary_key=True)
    book_id = models.IntegerField()
    bookshelf_id = models.IntegerField()
    
    def __str__(self):
        return 'Shelf Id: '+str(self.bookshelf_id)

class bookshelf(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return 'Name: '+str(self.name)

class book_languages(models.Model):
    id = models.IntegerField(primary_key=True)
    book_id = models.IntegerField()
    language_id = models.IntegerField()
    
    def __str__(self):
        return 'language Id: '+str(self.language_id)

class language(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=4)

    def __str__(self):
        return 'language Code: '+str(self.code)

class book_subjects(models.Model):
    id = models.IntegerField(primary_key=True)
    book_id = models.IntegerField()
    subject_id = models.IntegerField()
    
    def __str__(self):
        return 'subject Id: '+str(self.subject_id)

class subject(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()

    def __str__(self):
        return 'Name: '+str(self.name)


class format(models.Model):
    id = models.IntegerField(primary_key=True)
    mime_type = models.CharField(max_length=32)
    url = models.TextField()
    book_id = models.IntegerField()

    def __str__(self):
        return 'Book Id: '+str(self.book_id)



