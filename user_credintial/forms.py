from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=60,
        required=True,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Username"}),
    )

    first_name = forms.CharField(
        max_length=60,
        required=True,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "First name"}),
    )

    last_name = forms.CharField(
        max_length=60,
        required=True,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Last name"}),
    )

    email = forms.EmailField(
        max_length=50,
        label="",
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Email address"}),
    )

    password1 = forms.CharField(
        label="",
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Password"}),
    )

    password2 = forms.CharField(
        label="",
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm password"}),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="",
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Username"}),
    )
    password = forms.CharField(
        label="",
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Password"}),
    )

# update profile
class ChangeUserData(UserChangeForm):
    password = None
    
    username = forms.CharField(
        label="",
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Username"}),
    )

    first_name = forms.CharField(
        label="",
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "First name"}),
    )

    last_name = forms.CharField(
        label="",
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Last name"}),
    )

    email = forms.EmailField(
        label="",
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Email address"}),
    )
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']