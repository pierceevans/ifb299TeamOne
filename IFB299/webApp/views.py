from django.shortcuts import render
from webApp.models import Customer, Car, Store, Time, Make, Order, Location
from django.views import generic
from django.shortcuts import get_object_or_404

def index(request):
    num_orders = Order.objects.all().count()
    num_customers = Customer.objects.count()

    context = {
        'num_orders': num_orders,
        'num_customers': num_customers,
    }

    return render(request, 'index.html', context)


def CustomerDetailView(request, customerID):
    customer = Customer.objects.get(pk=customerID)
    orders = Order.objects.all()

    context = {
        'customer': customer,
        'orders': orders,
    }

    return render(request, 'Customer/customer_detail.html', context)

def OrderDetailView(request, orderID):
    order = Order.objects.get(pk=orderID)
    context = {
        'order': order,
    }

    return render(request, 'Customer/order_detail.html', context)



class CustomerListView(generic.ListView):
    model = Customer
    context_object_name = 'customer_list'
    template_name = 'Customer/customer_list.html'
