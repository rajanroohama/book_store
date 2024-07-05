# urls.py

from django.urls import path
from .views import index, books, cart, addtocart, updatecart, remove_from_cart, orders, placeorder, order_confirmation

urlpatterns = [
    path('', index, name='index'),
    path('books/', books, name='books'),
    path('orders/', orders, name='orders'),
    path('cart/', cart, name='cart'),
    path('cart/add/<int:bookid>/', addtocart, name='addtocart'),
    path('cart/update/<int:bookid>/<str:action>/', updatecart, name='updatecart'),
    path('cart/remove/<int:bookid>/', remove_from_cart, name='remove_from_cart'),
    path('placeorder/', placeorder, name='placeorder'),
    path('order_confirmation/', order_confirmation, name='order_confirmation'),
]
