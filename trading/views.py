from django.shortcuts import render

def order_book(request):
    return render(request, "trading/order_book.html")


from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderSerializer
# 🔹 List all orders & Create a new order
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create orders

    def perform_create(self, serializer):
        # Assign the logged-in user to the order
        serializer.save(user=self.request.user)

# 🔹 Retrieve, Update & Delete order by ID
class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access

    def get_queryset(self):
        # Ensure users can only view their own orders unless they are admin
        if self.request.user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user)