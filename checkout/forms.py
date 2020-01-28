from django import forms
from .models import Address
from .models import Order


# Create a form to allow users to enter Billing Address
class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = (
            'full_name', 'phone_number', 'address_line_1', 'address_line_2',
            'town', 'county', 'postcode'
        )
