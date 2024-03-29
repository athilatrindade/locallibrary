#aqui está se registrando os modelos e personalizando a apresentação de seus 
#dados, de modo a modificar a apresentação para forma diferente do padrão admin
from django.contrib import admin

# Register your models here.

from django.contrib import admin

# Register your models here.

from .models import Book, Author, Genre, BookInstance, Language

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)

class BooksInline(admin.TabularInline):
    model = Book

class AuthorAdmin(admin.ModelAdmin):
   list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

   fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
   #fields define que os campos serão mostrados na vertical (exceto aqueles juntos entre parênteses, data de nascimento e morte)

   inlines = [BooksInline]
   #faz com que as informações sobre os livros relacionados ao autor apareçam no detalhamento de cada autor

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


class BooksInstanceInline(admin.TabularInline):
     model = BookInstance


# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    
    inlines = [BooksInstanceInline]
    #faz com que as BookInstances (ou seja, as cópias dos livros) apareçam juntamente com o detalhamento de cada livro

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
     list_display = ('id', 'book','imprint', 'due_back', 'status','borrower')
     
     list_filter = ('status', 'due_back')
     #adiciona um filtro no painel de visualização das cópias dos livros
     #o filtro é baseado nos atributos status e due_back
     
     fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
    #agrupa os atributos das cópias dos livros em dois grupos diferentes
    #None e Availability  

