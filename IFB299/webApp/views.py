from webApp.models import Customer, Car, Store, Time, Make, Order, Location
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def index(request):
    carlist = Car.objects.all().order_by('car_id')
    makelist = Make.objects.values('car_make_name').distinct().order_by('car_make_name')
    car_fuelsystem_list = Car.objects.values('car_fuelsystem').distinct().order_by('car_fuelsystem')
    car_drive_list = Car.objects.values('car_drive').distinct().order_by('car_drive')
    car_seating = Car.objects.values('car_seatingcapacity').distinct().order_by('car_seatingcapacity')
    car_body = Car.objects.values('car_bodytype').distinct().order_by('car_bodytype')
    context = {
        'carlist' : carlist,
        'makelist' : makelist,
        'car_fuelsystem_list' : car_fuelsystem_list,
        'car_drive_list' : car_drive_list,
        'car_seating' : car_seating,
        'car_body' : car_body,
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

def CarDetailView(request, carID):
    car = Car.objects.get(pk=carID)
    make = Make.objects.all()

    context = {
        'car': car,
        'make' : make,
    }

    return render(request, 'Car/car_detail.html', context)


def OrderDetailView(request, orderID):
    order = Order.objects.get(pk=orderID)
    context = {
        'order': order,
    }

    return render(request, 'Customer/order_detail.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def all_cars(request):
    carlist = Car.objects.all().order_by('car_id')
    makelist = Make.objects.all().order_by('car_make_key')
    c_results = Make.objects.raw('''SELECT * FROM ifb299_database.car c
                INNER JOIN ifb299_database.make m
                ON c.Car_Make_Key = m.Car_Make_Key
                ORDER BY c.Car_ID;''')
    context = {
        'carlist' : carlist,
        'makelist' : makelist,
        'c_results' : c_results
    }
    return render(request, 'all_cars.html', context)

def search_results(request):
    if request.method == 'POST':
        make = request.POST.get('make')
        model = request.POST.get('model')
        fuel = request.POST.get('fuel')
        drive = request.POST.get('drive')
        seating = request.POST.get('seating')
        body = request.POST.get('body')
        my_dict = {
        }
        if make == "any":
            my_dict['make'] = "%"
        else:
            my_dict['make'] = make
        if model == "any":
            my_dict['model'] = "%"
        else:
            my_dict['model'] = model
        if fuel == "any":
            my_dict['fuel'] = "%"
        else:
            my_dict['fuel'] = fuel
        if drive == "any":
            my_dict['drive'] = "%"
        else:
            my_dict['drive'] = drive
        if seating == "any":
            my_dict['seating'] = "%"
        else:
            my_dict['seating'] = seating
        if body == "any":
            my_dict['body'] = "%"
        else:
            my_dict['body'] = body

        c_results = Make.objects.raw('''SELECT * FROM ifb299_database.car c
                                        INNER JOIN ifb299_database.make m
                                        ON c.Car_Make_Key = m.Car_Make_Key
                                        WHERE m.Car_Make_Name LIKE %(make)s AND
                                        m.Car_Model LIKE %(model)s AND
                                        c.Car_FuelSystem LIKE %(fuel)s AND
                                        c.Car_Drive LIKE %(drive)s AND
                                        c.Car_SeatingCapacity LIKE %(seating)s AND
                                        c.Car_BodyType LIKE %(body)s
                                        ORDER BY c.Car_ID;''', my_dict)

        print(c_results)

        context = {
            'c_results' : c_results
        }
        return render(request, 'search_results.html', context)
    else:
        return redirect('index')

class CustomerListView(generic.ListView):
    model = Customer
    context_object_name = 'customer_list'
    template_name = 'Customer/customer_list.html'
