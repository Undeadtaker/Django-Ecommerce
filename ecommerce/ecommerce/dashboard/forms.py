from django import forms

from ecommerce.users.models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['full_name', 'phone', 'town_city', 'postcode', 'address_line']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.fields['full_name'].widget.attrs.update({
            'class': 'form-control account-form input-sm', 'placeholder': 'Full Name'
        })

        self.fields["phone"].widget.attrs.update(
            {"class": "form-control account-form input-sm", "placeholder": "Phone"}
        )

        self.fields["address_line"].widget.attrs.update(
            {"class": "form-control account-form input-sm", "placeholder": "Full Name"}
        )
        self.fields["town_city"].widget.attrs.update(
            {"class": "form-control account-form input-sm", "placeholder": "Full Name"}
        )
        self.fields["postcode"].widget.attrs.update(
            {"class": "form-control account-form input-sm", "placeholder": "Full Name"}
        )
