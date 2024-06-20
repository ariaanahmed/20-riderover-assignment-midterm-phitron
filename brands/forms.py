from django import forms
from .models import Brands


class BrandsForm(forms.ModelForm):
    class Meta:
        model = Brands
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter brand name"}),
        }

        labels = {
            "name": "",
        }
