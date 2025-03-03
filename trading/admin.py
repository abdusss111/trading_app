from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'order_type', 'quantity', 'price', 'created_at')
    search_fields = ('user__username', 'product__name', 'order_type')
    list_filter = ('order_type', 'created_at')
