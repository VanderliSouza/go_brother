from django.contrib import admin

from gobrother.models import Book


class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)
