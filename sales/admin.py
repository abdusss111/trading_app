from django.contrib import admin
from .models import SalesOrder, Invoice

@admin.register(SalesOrder)
class SalesOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'total_price', 'created_at')
    search_fields = ('user__username', 'product__name')
    list_filter = ('created_at',)

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'sales_order', 'invoice_pdf', 'created_at')
    search_fields = ('sales_order__id',)
    list_filter = ('created_at',)
