# models.py

from django.db import models

class Books(models.Model):
    name = models.CharField(max_length=100)
    des = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.CharField(max_length=2083)

class Cart(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.book.price * self.quantity
