from books.models import all_book, book, author, book_authors, book_bookshelves, book_languages, book_subjects, bookshelf, format, language, subject
from rest_framework import serializers
from django.http import JsonResponse
from django.core.serializers import serialize

class class_sample(serializers.ModelSerializer):
    class Meta:
        model = book
        fields='__all__'

def generate_data(request):
    allbooks=book.objects.all()
    check_all_books=all_book.objects.all()
    data_id = 0
    data_title = ''
    data_author = ''
    data_genre = ''
    data_language = ''
    data_subjects = ''
    data_bookshelves = ''
    data_download_links = ''
    data_mime_type = ''

    if len(check_all_books)==0:
        for i in allbooks:
            id=i.id
            data_id = i.id
            data_title = i.title
            
            # author=author_names
            auth_id=book_authors.objects.filter(book_id=id)
            auth_name_list = []
            for j in auth_id:
                auth_name = author.objects.filter(id=j.author_id).values_list('name', flat=True).first()
                if auth_name:
                    auth_name_list.append(auth_name)
            data_author = ', '.join(auth_name_list)

            # language=language_code
            lang_id=book_languages.objects.filter(book_id=id)
            lang_code_list = []
            for j in lang_id:
                lang_code = language.objects.filter(id=j.language_id).values_list('code', flat=True).first()
                if lang_code:
                    lang_code_list.append(lang_code)
            data_language = ', '.join(lang_code_list)

            # subject=subject_name
            sub_id=book_subjects.objects.filter(book_id=id)
            sub_name_list = []
            for j in sub_id:
                sub_name = subject.objects.filter(id=j.subject_id).values_list('name', flat=True).first()
                if sub_name:
                    sub_name_list.append(sub_name)
            data_subjects = ', '.join(sub_name_list)

            # bookshelve
            bookshelve_name=book_bookshelves.objects.filter(book_id=id)
            bookshelve_name_list = []
            for j in bookshelve_name:
                shelf_name = bookshelf.objects.filter(id=j.bookshelf_id).values_list('name', flat=True).first()
                if shelf_name:
                    bookshelve_name_list.append(shelf_name)
            data_bookshelves = ', '.join(bookshelve_name_list)


            # download_link=
            down_link=format.objects.filter(book_id=id)
            down_link_list = []
            for j in down_link:
                link = format.objects.filter(id=j.book_id).values_list('url', flat=True).first()
                if link:
                    down_link_list.append(link)

            data_download_links = ', '.join(down_link_list)

            # genre=subject+bookshelf
            data_genre = data_subjects+', '+data_bookshelves

            # mime_type
            mime_type=format.objects.filter(book_id=id)
            mime_type_list = []
            for j in mime_type:
                og_type = format.objects.filter(id=j.book_id).values_list('mime_type', flat=True).first()
                if og_type:
                    mime_type_list.append(og_type)

            data_mime_type = ', '.join(mime_type_list)

            query = all_book.objects.create(id= data_id, title = data_title, author = data_author, genre = data_genre, 
            language = data_language, subjects = data_subjects, bookshelves = data_bookshelves, download_links = data_download_links, mime_type = data_mime_type)

    all_sample = book.objects.all()
    sample_serial=class_sample(all_sample,many=True)
    serialized_data = sample_serial.data
    return JsonResponse(serialized_data, safe=False)
