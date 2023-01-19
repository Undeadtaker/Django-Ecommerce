from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserNameChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control account-form input-sm', 'placeholder': str('Current name:')
        })

