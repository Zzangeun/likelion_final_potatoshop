from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = {'product', 'orderer', 'postcode', 'address', 'phone1', 'phone2', 'email', 'message', 'price', 'delivery_price', 'total_price',}