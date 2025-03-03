from django.urls import path
from .views import generate_invoice
from .views import SalesOrderListCreateView, SalesOrderDetailView, InvoiceListCreateView, InvoiceDetailView

urlpatterns = [
    path("invoice/<int:order_id>/", generate_invoice, name="generate_invoice"),
    path('sales-orders/', SalesOrderListCreateView.as_view(), name='sales-order-list-create'),
    path('sales-orders/<int:pk>/', SalesOrderDetailView.as_view(), name='sales-order-detail'),
    path('invoices/', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('invoices/<int:pk>/', InvoiceDetailView.as_view(), name='invoice-detail'),

]
