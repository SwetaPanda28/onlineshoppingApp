from django.forms import ModelForm
from . import models

class AddressForm(ModelForm):
    class Meta:
        model=models.Address
        fields="__all__"