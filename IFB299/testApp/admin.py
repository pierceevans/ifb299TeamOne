from django.contrib import admin
from testApp.models import Customer

#admin.site.register(Customer)

# Define the admin class
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'customer_name')
    list_filter = ('customer_id', 'customer_name')

# Register the admin class with the associated model
admin.site.register(Customer, CustomerAdmin)
