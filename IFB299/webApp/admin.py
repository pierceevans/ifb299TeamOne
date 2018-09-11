from django.contrib import admin
from .models import Customer
from .models import Location
from .models import Make
from .models import Order
from .models import Store
from .models import Time
from .models import Car


admin.site.register(Customer)
admin.site.register(Location)
admin.site.register(Make)
admin.site.register(Order)
admin.site.register(Store)
admin.site.register(Time)
admin.site.register(Car)
