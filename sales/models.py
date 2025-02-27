from django.db import models

class SalesOrder(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class Invoice(models.Model):
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    invoice_pdf = models.FileField(upload_to='invoices/')
    created_at = models.DateTimeField(auto_now_add=True)
