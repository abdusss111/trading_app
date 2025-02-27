from django.shortcuts import render

def order_book(request):
    return render(request, "trading/order_book.html")
