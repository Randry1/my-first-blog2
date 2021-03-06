from django.contrib import admin

# Register your models here.
from .models import Author, Book, Genre, Language, Status, BookInstance

# admin.site.register(Author)
# admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
# admin.site.register(BookInstance)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name']


class BookInstanceInline(admin.TabularInline):
    """Класс одновременное отображение связаных моделей в линию"""
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'display_author')
    # fields = ['title', 'genre']
    # exclude = ['genre']  # удалить поля из форм редактирования
    list_filter = ('genre', 'author')
    inlines = [BookInstanceInline]

    
@admin.register(BookInstance)
class BookInstance(admin.ModelAdmin):
    # list_display = ['inv_nom', 'book', 'imprint', 'status']
    #  Обьеденяем поля по группам в админке сайта
    list_filter = ('book', 'status')
    fieldsets = (
        ('Экземпляр книги', {'fields': ('book', 'imprint', 'inv_nom')}),
        ('Статус и окончание его срока действия', {'fields': ('status', 'due_back')})
    )
