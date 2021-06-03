# Django
from django.forms import ModelForm, fields

# Models
from .models import Order


class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = '__all__'