from django.forms import ModelForm
from .models import FoundItems

class CreationForm(ModelForm):
    title = 
    class Meta:
        model = FoundItems
        fields = ['title', 'textfield', 'image', 'category', 'phonenumber', 'email']


