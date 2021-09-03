from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)

class UserCreateForm(UserCreationForm):
            
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )


    class Meta:
        model = User
        fields = ("username","first_name", "email", "password1", "password2")
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
         
        }



class UserUpdateForm(forms.ModelForm):
     class Meta:
         model = User
         fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
     class Meta:
         model = Profile
         fields = ['image']