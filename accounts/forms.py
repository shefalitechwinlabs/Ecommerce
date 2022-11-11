from django import forms
from .models import *
from django.contrib.auth.password_validation import validate_password


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}),validators=[validate_password])
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'confirm_password'}),validators=[validate_password])
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'first_name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'last_name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'email'}))
   
    class Meta:
        model = ExtendUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    # Password match validator function
    def clean_password(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        print(password,confirm_password)
        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError(
                    'password and confirm_password does not match'
                )    

class Address(forms.ModelForm):

    class Meta:
        model = Address
        fields = "__all__"