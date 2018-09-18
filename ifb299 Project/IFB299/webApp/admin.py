from django.contrib import admin
from .models import Customer
from .models import Location
from .models import Make
from .models import Order
from .models import Store
from .models import Time
from .models import Car

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'customer_name', 'customer_phone', 'customer_address')
    list_filter = ('customer_id', 'customer_name', 'customer_phone', 'customer_address')

admin.site.register(Customer, CustomerAdmin)

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_id', 'car_make_key', 'car_series_year')
    list_filter = ('car_id', 'car_make_key', 'car_series_year')

admin.site.register(Car, CarAdmin)


admin.site.register(Location)
admin.site.register(Make)
admin.site.register(Order)
admin.site.register(Store)
admin.site.register(Time)
