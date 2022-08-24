from django.forms import ModelForm
from django import forms
from .models import FoundItems
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CreationForm(ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Title'}
        )
    )
    textfield = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'More info'}
        )
    )
    phonenumber = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'E.g. 87473339140'}
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'E.g. a.aussarbekov@gmail.com'}
        )
    )
    class Meta:
        model = FoundItems
        fields = ['title', 'textfield', 'image', 'category', 'phonenumber', 'email']


