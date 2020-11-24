from django.contrib import admin
from cars.models import Miles, Fuel, Body, Transmission, Features, CarDetails

# Register your models here.
admin.site.register(Miles)
admin.site.register(Fuel)
admin.site.register(Body)
admin.site.register(Transmission)
admin.site.register(Features)
admin.site.register(CarDetails)
