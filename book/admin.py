from django.contrib import admin

# from book_project import Book
from .models import Book
from .models import LibUser

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'rasm',
        'kg'
    )

@admin.register(LibUser)
class Libuser(admin.ModelAdmin):
    list_display = (
        'id',
        'fakaferi',
        'jerjero'
    )
# admin.site.register(Book)
