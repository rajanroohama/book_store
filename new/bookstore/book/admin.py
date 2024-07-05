# admin.py

from django.contrib import admin
from .models import Books, Cart

class BooksAdmin(admin.ModelAdmin):
    list_display = ('name', 'des', 'price', 'image')

class CartAdmin(admin.ModelAdmin):
    list_display = ('book', 'quantity')

admin.site.register(Books, BooksAdmin)
admin.site.register(Cart, CartAdmin)
