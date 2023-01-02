from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm

from .models import CustomUser, Address


# ---------------------------------------------------------------- #

class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(label='Username',
                                min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(label = 'Email', max_length=50, help_text='Required',
                                error_messages={'required': 'Email is a required field.'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('user_name', 'email',)

    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        potential_user = CustomUser.objects.filter(user_name=user_name)
        if potential_user.count():
            raise forms.ValidationError('Username already exists')
        return potential_user

    def clean_confirm_password(self):
        data = self.cleaned_data
        if data['password'] != data['confirm_password']:
            raise forms.ValidationError('Passwords do not match')
        return data['confirm_password']

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        potential_user = CustomUser.objects.filter(email=email)
        if CustomUser.objects.filter(user_name=email).exists():
            raise forms.ValidationError('Email already exists, please use a different email address')
        return email


    # Access fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update({
            'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({
            'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email'})
        self.fields['password'].widget.attrs.update({
            'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['confirm_password'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Confirm Password'})

# ---------------------------------------------------------------- #

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3',
               'placeholder': 'Username',
               'id': 'login-username'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'placeholder': 'Password',
               'id': 'login-password'}
    ))

# ---------------------------------------------------------------- #

class UserEditForm(forms.ModelForm):
    email = forms.EmailField(
        label = 'Email (cannot be changed)', max_length=200,
        widget=forms.TextInput(
            attrs =
                {
                    'class': 'form-control mb-3',
                    'placeholder': 'email',
                    'id': 'form-email',
                    'readonly': 'readonly'
                }
        )
    )

    user_name = forms.CharField(
        label = 'Username', min_length=4, max_length=50, widget=forms.TextInput(
            attrs=
            {
                'class': 'form-control mb-3',
                'placeholder': 'Username',
                'id': 'form-username',
                'readonly': 'readonly'
            }
        )
    )

    first_name = forms.CharField(
        label='Firstname', min_length=4, max_length=50, widget=forms.TextInput(
            attrs=
            {
                'class': 'form-control mb-3',
                'placeholder': 'Firstname',
                'id': 'form-firstname'
            }
        )
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'user_name', 'first_name')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].required = True
        self.fields['email'].required = True

# ---------------------------------------------------------------- #

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=255, widget=forms.TextInput(
        attrs= {
            'class': 'form-control mb-3',
            'placeholder': 'Email',
            'id': 'form-email'
        }
    ))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = CustomUser.objects.filter(email=email)
        if not user:
            raise forms.ValidationError('Account not found.')
        return email

# ---------------------------------------------------------------- #

class MyPasswordConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(label = 'Enter new password', widget=forms.PasswordInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-password'}
    ))

    new_password2 = forms.CharField(label = 'Confirm new password', widget=forms.PasswordInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-confirm'}
    ))

# ---------------------------------------------------------------- #

class UserAddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ['full_name', 'phone', 'address_line', 'address_line2', 'town_city', 'postcode']

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
        self.fields["address_line2"].widget.attrs.update(
            {"class": "form-control account-form input-sm", "placeholder": "Full Name"}
        )
        self.fields["town_city"].widget.attrs.update(
            {"class": "form-control account-form input-sm", "placeholder": "Full Name"}
        )
        self.fields["postcode"].widget.attrs.update(
            {"class": "form-control account-form input-sm", "placeholder": "Full Name"}
        )


















