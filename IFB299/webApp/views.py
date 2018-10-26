from webApp.models import Customer, Car, Store, Time, Make, Order, Location
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.gis.geoip2 import GeoIP2


def index(request):
    carlist = Car.objects.all().order_by('car_id')
    makelist = Make.objects.values('car_make_name').distinct().order_by('car_make_name')
    car_fuelsystem_list = Car.objects.values('car_fuelsystem').distinct().order_by('car_fuelsystem')
    car_drive_list = Car.objects.values('car_drive').distinct().order_by('car_drive')
    car_seating = Car.objects.values('car_seatingcapacity').distinct().order_by('car_seatingcapacity')
    car_body = Car.objects.values('car_bodytype').distinct().order_by('car_bodytype')
    postcode = Location.objects.values('postcode').distinct().order_by('postcode')
    context = {
        'carlist' : carlist,
        'makelist' : makelist,
        'car_fuelsystem_list' : car_fuelsystem_list,
        'car_drive_list' : car_drive_list,
        'car_seating' : car_seating,
        'car_body' : car_body,
        'postcode' : postcode,
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
    #Finds the apprpriate car object for the given key
    car = Car.objects.get(pk=carID)
    #Gets all make objects
    make = Make.objects.all()
    #Saves them to context
    order = Order.objects.get(car=carID)

    context = {
            'car': car,
            'make' : make,
            'order' : order,
    }
    #Renders page with context attached
    return render(request, 'Car/car_detail.html', context)


def OrderDetailView(request, customerID, orderID):
    order = Order.objects.get(pk=orderID)
    make = Make.objects.all()
    customer = Customer.objects.all()
    car = Car.objects.all()
    location = Location.objects.all()
    store = Store.objects.all()
    date = Time.objects.all()
    context = {
        'order': order,
        'make' : make,
        'customer' : customer,
        'car' : car,
        'location' : location,
        'store' : store,
        'date' : date,
    }

    return render(request, 'Customer/order_detail.html', context)

def signup(request):
    #Checks to see if the request is POST or GET. If it is post, it has
    #been sent by the server, as specified in the 'action' method of
    #the form
    if request.method == 'POST':
        #Gets the form from the request
        form = UserCreationForm(request.POST)
        #Checks to see if the form is valid
        if form.is_valid():
            #Saves the form
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            #Gets the username and password from the form, before authenticating
            #and logging the user in
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            #Redirects user to home page
            return redirect('index')
    else:
        #Shows unfilled form if request is GET (Sent by the user)
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

def all_stores(request):

    return render(request, 'all_stores')

def staffPortal(request):

    return render(request, 'Staff/portal.html')

def customerList(request):
    customerlist = Customer.objects.all()
    context = {
        'customerlist' : customerlist
    }
    return render(request, 'Staff/customer_list.html', context)

def orderList(request):
    return render(request, 'Staff/order_list.html')

def reportsView(request):
    return render(request, 'Staff/reports.html')

def aboutView(request):
    return render(request, 'about-us.html')

def storeDetailView(request, store_id):
    store = Store.objects.get(pk=store_id)
    context = {
        'store' : store
    }
    return render(request, 'Store/store_detail.html', context)

def mapView(request):
    storelist = Store.objects.all()
    locationlist = Location.objects.all()
    context = {
        'storelist' : storelist,
        'locationlist' : locationlist,
    }
    return render(request, 'store-map.html', context)

def search_results(request):
    #Checks to see if the page is being requestd
    #using POST. This is to check if the page is
    #being requested by a user or the server.
    if request.method == 'POST':
        #Gets all the data from the forms and
        #sets it to variables
        make = request.POST.get('make')
        model = request.POST.get('model')
        fuel = request.POST.get('fuel')
        drive = request.POST.get('drive')
        seating = request.POST.get('seating')
        body = request.POST.get('body')
        #Creates an empty dictionary
        my_dict = {
        }
        #For each variable, checks if the
        #user has set the form to include all
        #results or has set a specific value,
        #before adding the value to the dictionary
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

        #SQL Query to select all the appropriate data from the database. This is
        #dependent on the options set by the user. This query makes use of parameters
        #that are decided at runtime, using the values set in the dictionary
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


        context = {
            'c_results' : c_results
        }
        #Renders the page
        return render(request, 'search_results.html', context)
    else:
        #Redirects user to the home page if they send a GET request
        return redirect('index')

class CustomerListView(generic.ListView):
    model = Customer
    context_object_name = 'customer_list'
    template_name = 'Customer/customer_list.html'
