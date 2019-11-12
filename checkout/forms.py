from django import forms
from .models import Address
from .models import Order


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = (
            'full_name', 'phone_number', 'address_line_1', 'address_line_2',
            'town', 'county', 'postcode'
        )