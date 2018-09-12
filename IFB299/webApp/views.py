from django.shortcuts import render
from webApp.models import Customer, Car, Store, Time, Make, Order, Location
from django.views import generic
from django.shortcuts import get_object_or_404

def customer_detail_view(request, primary_key):
    customer = get_object_or_404(Customer, pk=customer.customer_id)
    return render(request, 'webApp/customer_detail.html', context={'customer': customer})

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
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
