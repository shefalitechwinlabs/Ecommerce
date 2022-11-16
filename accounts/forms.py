from django import forms
from .models import *
from django.contrib.auth.password_validation import validate_password


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}),validators=[validate_password])
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'confirm_password'}),validators=[validate_password])
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'email'}))
   
    class Meta:
        model = ExtendUser
        fields = ['username', 'email','password', 'confirm_password']

    # Password match validator function
    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        #print(cleaned_data)
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        print(confirm_password)
        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError(
                    'password and confirm_password does not match'
                )    

class AddressForm(forms.ModelForm):
    address_type = forms.CharField(widget=forms.Select(choices=address_choices,attrs={'placeholder': 'address_type'}))
    building = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'building number'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'city'}))
    sector = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'sector or nagar'}))
    district = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'district'}))
    state = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'state'}))
    pincode = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'pincode'}))
    locality = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'locality/colony'}))
    contact = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'contact'}))
    

    class Meta:
        model = Address
        exclude = ['created_by', 'updated_on', 'updated_on']

class ProfileForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'name'}))
    image = forms.ImageField()
    bio = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'bio'}))
    

    class Meta:
        model = Profile
        exclude = ['created_by', 'updated_on', 'updated_on']
