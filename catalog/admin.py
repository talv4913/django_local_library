from django.contrib import admin
from .models import Book, BookInstance, Author, Genre, Language

# Register your models here.

#admin.site.register(Book)
#admin.site.register(BookInstance)
#admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)

class BooksInline(admin.TabularInline):
    """clase para agregar inline de book a  la clase Author"""
    model = Book
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]

admin.site.register(Author,AuthorAdmin)

class BooksInstancesInline(admin.TabularInline):
    """clase para agregar inline a la clase Book"""
    model = BookInstance
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'isbn')

    inlines = [BooksInstancesInline]



@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display  = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),

        ('Availability', {
            'fields': ('status', 'due_back')
        })

    )