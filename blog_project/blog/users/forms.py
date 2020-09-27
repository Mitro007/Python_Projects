from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):

    # default is required=True
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        # password2 is for password confirmation
        fields = ['username', 'email', 'password1', 'password2']
        