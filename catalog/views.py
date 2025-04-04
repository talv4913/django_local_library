from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre

from django.views import generic

# Create your views here.

def index(request):

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    #challenge yourself part
    num_genres = Genre.objects.count()
    num_hola_in_book = Book.objects.filter(title__icontains='hola').count()

    #Available books
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()


    #The all is implied by default
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres' : num_genres,
        'num_hola_in_book' : num_hola_in_book,
    }

    return render(request ,'index.html', context=context)



class BookListView(generic.ListView):
    model = Book

