# Django
from django.contrib import admin

# Models
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)