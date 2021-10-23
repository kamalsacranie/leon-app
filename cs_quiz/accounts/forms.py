from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Inherit from the user creation form to add our own fields
class SignUpForm(UserCreationForm):
    """User creation form with custom fields. User has no privelages"""

    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(
        max_length=254, required=True, help_text="School Email"
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )
