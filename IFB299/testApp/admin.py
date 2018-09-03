from django.contrib import admin
from testApp.models import Customer

#admin.site.register(Customer)

# Define the admin class
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('Customer_ID', 'Customer_Name')
    list_filter = ('Customer_ID', 'Customer_Name')

# Register the admin class with the associated model
admin.site.register(Customer, CustomerAdmin)
