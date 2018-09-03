from django.shortcuts import render

def index(request):
    if request and request.method == 'GET':

        from models import Customer

        if customer.objects.count() != 0:
            for i in range(customer.objects.count()):
                editCustomer = Customer.objects.get(id = i)
                editCustomer.Customer_Name = Customer.objects.get(Customer_Name)
                editCustomer.Customer_Phone = Customer.objects.get(Customer_Phone)
                editCustomer.Customer_Address = Customer.objects.get(Customer_Address)
                editCustomer.Customer_Occupation = Customer.objects.get(Customer_Occupation)
                editCustomer.Customer_Birthday = Customer.objects.get(Customer_Birthday)
                editCustomer.Customer_Gender = Customer.objects.get(Customer_Gender)
                editCustomer.save()
