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

    return render(request, 'index.html', context=context)


class CustomerListView(generic.ListView):
    model = Customer
    context_object_name = 'customer_list'
    template_name = 'Customer/customer_list.html'

class CustomerDetailView(generic.DetailView):
    model = Customer


class OrderListView(generic.ListView):
    model = Order
    context_object_name = 'order_list'
    template_name = 'Order/order_list.html'
