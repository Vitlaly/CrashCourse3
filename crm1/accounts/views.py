from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_orders = orders.count()
    total_customers = customers.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {
        'orders': orders,
        'customers': customers,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending
    }

    return render(request, 'accounts/dashboard.html', context)


def products(request):
    product = Product.objects.all()

    return render(request, 'accounts/products.html', {'product': product})


def customer(request, test_pk):
    customer = Customer.objects.get(id=test_pk)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {'customer': customer, 'orders': orders, 'orders_count': order_count}
    return render(request, 'accounts/customer.html', context)

