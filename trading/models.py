from django.db import models

class Order(models.Model):
    BUY = 'buy'
    SELL = 'sell'
    ORDER_TYPES = [(BUY, 'Buy'), (SELL, 'Sell')]

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    order_type = models.CharField(max_length=4, choices=ORDER_TYPES)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
