from io import BytesIO
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import SalesOrder

def generate_invoice(request, order_id):
    try:
        order = SalesOrder.objects.get(id=order_id)

        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        pdf.drawString(100, 800, f"Invoice for Order {order.id}")
        pdf.drawString(100, 780, f"Customer: {order.user.username}")
        pdf.drawString(100, 760, f"Product: {order.product.name}")
        pdf.drawString(100, 740, f"Quantity: {order.quantity}")
        pdf.drawString(100, 720, f"Total Price: ${order.total_price}")
        pdf.drawString(100, 700, f"Date: {order.created_at}")
        pdf.showPage()
        pdf.save()

        buffer.seek(0)
        response = HttpResponse(buffer, content_type="application/pdf")
        response["Content-Disposition"] = f'attachment; filename="invoice_{order_id}.pdf"'
        return response

    except SalesOrder.DoesNotExist:
        return HttpResponse("Order not found", status=404)


from rest_framework import generics, permissions
from .models import SalesOrder, Invoice
from .serializers import SalesOrderSerializer, InvoiceSerializer

# List & Create Sales Orders
class SalesOrderListCreateView(generics.ListCreateAPIView):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

# Retrieve, Update & Delete a Sales Order
class SalesOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

# List & Create Invoices
class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

# Retrieve, Update & Delete an Invoice
class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

