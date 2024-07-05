# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Books, Cart

def index(request):
    return render(request, "index.html")

def books(request):
    book_list = Books.objects.all()
    return render(request, 'books.html', {'books': book_list})

def cart(request):
    cart_items = Cart.objects.all()
    total_amount = sum(item.total_price for item in cart_items)
    return render(request, "cart.html", {'cartitems': cart_items, 'total_amount': total_amount})

def addtocart(request, bookid):
    book = get_object_or_404(Books, pk=bookid)
    cart_item, created = Cart.objects.get_or_create(book=book)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

def updatecart(request, bookid, action):
    cart_item = get_object_or_404(Cart, book_id=bookid)
    if action == 'increase':
        cart_item.quantity += 1
    elif action == 'decrease':
        cart_item.quantity -= 1
        if cart_item.quantity <= 0:
            cart_item.delete()
            return redirect('cart')
    cart_item.save()
    return redirect('cart')

def remove_from_cart(request, bookid):
    cart_item = get_object_or_404(Cart, book_id=bookid)
    cart_item.delete()
    return redirect('cart')

def orders(request):
    cart_items = Cart.objects.all()
    total_amount = sum(item.total_price for item in cart_items)
    print(f"Total Amount Calculated: {total_amount}")  # Add this line for debugging
    return render(request, "orders.html", {'cartitems': cart_items, 'total_amount': total_amount})


def placeorder(request):
    if request.method == 'POST':
        Cart.objects.all().delete()
        return redirect('order_confirmation')
    else:
        messages.error(request, 'Invalid request method')
        return redirect('orders')
    
def order_confirmation(request):
    return render(request, 'order_confirmation.html')
